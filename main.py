from PIL import Image
from math import ceil


#this function maintains aspect ratio, so no worries
def width_resize_and_convert(filepath: str, output_filepath: str, width: int, output_format: str | None = None) -> None :
    try:
        with Image.open(filepath, "r") as image:

            multiplier_height: float | int = image.size[1] / image.size[0]
            resized_image: Image = image.resize((width, ceil(width * multiplier_height))) #ceil, so that it doesn't cause errors with very small images becuase of the height
            resized_image.save(output_filepath, format=output_format if output_format[0] != "." else output_format[1:]) #so that inputs starting with "." work)

    except PermissionError as p:
        print(f"The error is {p}")


#resize_and_convert("placeholder.png", r"imgs/placeholder.webp", width=500, output_format="webp") #example


def many_imgs(filepath: str, output_filepath_noname: str, name: str, output_format: str, width: int, increment: int, times: int) -> None:

    for i in range(times):
        width_resize_and_convert(rf'{filepath}',
                           rf'{output_filepath_noname}/{name}-{width + increment * i}.{output_format if output_format[0] != "." else output_format[1:]}',
                           width=width + increment * i,
                           output_format=output_format) #make sure the arguments use double quotes because it breaks with single quotes


#many_imgs(r"C:\Users\exampleuser\Downloads\downaloadedimg.jpg",
#          r"C:\Users\exampleuser\imgfolder\",
#          "exampleimg",
#          3,
#          1000,
#          500,
#          "webp")
#this is an example of how it should look like


def main():
    try:
        filepath: str = input("What's the filepath for the original image?: ")
        output_filepath_noname: str = input("What's the directory/folder for your new images?: ")
        name: str = input("What should be the file name for your new images?: ")
        output_format: str = input("What's the format of the new images?: ")

        while True:
            try:
                width: int = int(input("What's the width of the new images be in pixels? (aspect ratio is maintained): "))
                break
            except ValueError as v:
                print(f"\n{v}\n")

        while True:
            try:
                increment: int = int(input("By how much should the new images increase in width (px) for each iteration?: "))
                break
            except ValueError as v:
                print(f"\n{v}\n")

        while True:
            try:
                times: int = int(input("For how many times?: "))
                break
            except ValueError as v:
                print(f"\n{v}\n")
        try:
            many_imgs(filepath, output_filepath_noname, name, output_format, width, increment, times)
        except Exception as e:
            print(f"\n{e}\n")

    except KeyboardInterrupt as k:
        print(k)


if __name__ == "__main__":
    main()
