import dronecan, datetime, time
from dronecan import uavcan
from argparse import ArgumentParser

# get command line arguments
parser = ArgumentParser(description='dump all DroneCAN messages')
parser.add_argument("--bitrate", default=1000000, type=int, help="CAN bit rate")
parser.add_argument("--node-id", default=100, type=int, help="CAN node ID")
parser.add_argument("--dna-server", action='store_true', default=False, help="run DNA server")
parser.add_argument("--port", default='can0', type=str, help="serial port")
args = parser.parse_args()

# Initializing a DroneCAN node instance.
node = dronecan.make_node(args.port, node_id=args.node_id, bitrate=args.bitrate)

# Initializing a node monitor, so we can see what nodes are online
node_monitor = dronecan.app.node_monitor.NodeMonitor(node)

if args.dna_server:
    # optionally start a DNA server
    dynamic_node_id_allocator = dronecan.app.dynamic_node_id.CentralizedServer(node, node_monitor)

# open file where all data temporally stored
file = open('temp_output.csv', 'w')
def handle_node_info(msg):
    '''
    Function is used in add_handler method. Handle message in format of csv
    :param msg:
    :return:
    '''
    print('{} {};{};{};{}'.format(datetime.date.today().strftime("%d/%m/%Y"),
                                (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%H:%M:%S"),
                                msg.transfer.source_node_id,
                                datetime.timedelta(seconds=int(str(dict(msg.transfer.payload._fields)['uptime_sec']))),
                                dict(msg.transfer.payload._fields)['health']), #file=file
          )

node.add_handler(uavcan.protocol.NodeStatus, handle_node_info)

try:
    # spin node for hour and gethering dataset
    node.spin(timeout=1) # timeout 3600?
except KeyboardInterrupt:
    quit()