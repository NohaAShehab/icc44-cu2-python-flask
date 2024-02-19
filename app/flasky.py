

## import function ---> entry point to run the application

from app import create_app

if __name__ == '__main__':
    app = create_app("prd")
    app.run(port=5001)