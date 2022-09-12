# Main bot code
from Utils.Connection import connection

def main():
    bot = connection()
    bot.run()
    
if __name__ == "__main__":
    main()