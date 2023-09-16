import instaloader

def download_instagram_photos(username):
    # Create an Instaloader instance
    loader = instaloader.Instaloader()

    try:
        # Retrieve the profile information
        profile = instaloader.Profile.from_username(loader.context, username)

        # Iterate over the profile's posts and download each photo
        for post in profile.get_posts():
            loader.download_post(post, target=f"{username}")

        print("Download completed.")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    username = input("Enter the Instagram username: ")
    download_instagram_photos(username)
