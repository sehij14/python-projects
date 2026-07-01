# Day34 
# Smart File Organizer

class FileUtility:

    @staticmethod
    def get_file_category(filename):

        filename = filename.lower()

        image_extensions = [".png", ".jpg", ".jpeg", ".gif"]
        document_extensions = [".pdf", ".docx", ".txt"]
        video_extensions = [".mp4", ".mkv"]
        audio_extensions = [".mp3", ".wav"]

        for extension in image_extensions:
            if filename.endswith(extension):
                return "Images"

        for extension in document_extensions:
            if filename.endswith(extension):
                return "Documents"

        for extension in video_extensions:
            if filename.endswith(extension):
                return "Videos"

        for extension in audio_extensions:
            if filename.endswith(extension):
                return "Audio"

        return "Others"

    @staticmethod
    def is_valid_filename(filename):

        if len(filename.strip()) == 0:
            return False

        if "." not in filename:
            return False

        return True


files = []

while True:

    print("\nSMART FILE ORGANIZER")
    print("1. Add File")
    print("2. Analyze Files")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        filename = input("Enter filename: ")

        if FileUtility.is_valid_filename(filename):
            files.append(filename)
            print("File added successfully.")
        else:
            print("Invalid filename.")

    elif choice == "2":

        if len(files) == 0:
            print("No files available.")

        else:

            print("\nFILE ANALYSIS")

            for file in files:

                category = FileUtility.get_file_category(file)

                print(f"{file} --> {category}")

    elif choice == "3":

        print("Closing Smart File Organizer.")
        break

    else:
        print("Invalid choice.")