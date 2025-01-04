import os
from PIL import Image
from pillow_heif import register_heif_opener

home_path = os.path.join(os.path.expanduser('~'))
desktop_path = os.path.join(home_path, "Desktop")
folder_path = os.path.join(desktop_path, "merge_logo_with_pics")


def main():
    register_heif_opener()
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
    else:
        os.rmdir(folder_path)
        os.mkdir(folder_path)

    input("Upload your pics and press Enter to continue...")

    logo_path = os.path.join(folder_path, "logo.png")
    if not os.path.exists(logo_path):
        print("Please enter a valid logo path")
        return
    else:
        with Image.open(logo_path) as logo:
            logo.load()
        #
        for path in os.listdir(folder_path):
            if path == "logo.png":
                continue

            paths = os.path.join(folder_path, path)
            with Image.open(paths) as jeans_pics:
                jeans_pics.load()
            # center  2862 / 2 - (211 / 2)
            position = round(jeans_pics.width / 2 - (211 / 2))
            jeans_pics.paste(logo, (position, 142), logo)

            jeans_pics.save(paths)
            jeans_pics.close()

    return


if __name__ == "__main__":
    main()
