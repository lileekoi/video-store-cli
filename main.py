import requests
from customer import Customer
from video import Video
from rental import Rental

URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    print("Please choose from the following menu options:")

    options = {
            "1": "add a video", 
            "2": "edit a video",
            "3": "delete a video", 
            "4": "get information about all videos",
            "5": "get information about one video",
            # "6": "add a customer",
            # "7": "edit a customer",
            # "8": "delete a customer",
            # "9": "get information about one customer",
            # "10": "get information about all customers",
            # "11": "check out a video to a customer",
            # "12": "check in a video from a customer"
            # "13": "Quit"
            }

    for choice_num in options:
            print(f"Option {choice_num}. {options[choice_num]}")

    return options

def make_choice(options, video):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option number: ")

    if choice in ['2','3'] and video.selected_video == None:
        print("You must select a video before editing it or deleting it")
        print("Let's select a video!")
        choice = "5"
    # elif choice in ['7','8'] and Customer.customer == None:
    #     print("You must select a customer before editing it or deleting it")
    #     print("Let's select a customer!")
    #     choice = "10"

    return choice

def run_cli(play=True):

    #initialize retro_video_store
    customer = Customer(URL="https://retro-video-store-api.herokuapp.com")
    video = Video(URL="https://retro-video-store-api.herokuapp.com")
    rental = Rental(URL="https://retro-video-store-api.herokuapp.com")

    # print choices
    options = main()

    while play==True:

        # get input and validate
        choice = make_choice(options, video)

        if choice=='1':
            print("Great! Let's create a new video.")
            title=input("What is the title of your video? ")
            release_date=input("What is the release date of your video? ")
            total_inventory=input("What is the total inventory of your video? ")
            available_inventory=input("What is the available inventory of your video? ")
            response = video.create_video(
                title=title, 
                release_date=release_date, 
                total_inventory=total_inventory,
                available_inventory=available_inventory
                )

            print("New video:", response["video"])

        elif choice=='2':
            print(f"Great! Let's update the video: {video.selected_video}")
            title=input("What is the new title of your video? ")
            release_date=input("What is the new release date of your task? ")
            response = video.update_video(title=title, release_date=release_date)

            print("Updated video:", response["video"])

        elif choice=='3':
            video.delete_video()

            print("Video has been deleted.")

            print(video.list_videos())

        elif choice=='4':
            for video in video.list_videos():
                print(video)
        elif choice=='5':
            select_by = input("Would you like to select by? Enter title or id: ")
            if select_by=="title":
                title = input("Which task title would you like to select? ")
                video.get_video(title=title)
            elif select_by=="id":
                id = input("Which task id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    video.get_video(id=id)
            else:
                print("Could not select. Please enter id or title.")
            
            if video.selected_video:
                print("Selected task: ", video.selected_video)

run_cli()

if __name__ == "__main__":
    main()