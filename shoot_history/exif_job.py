import exiftool
from colorama import Fore, Back, Style
import re



def change_color_class(file, image_title, color):
    with exiftool.ExifToolHelper() as et:
        et.set_tags(
            [file],
            tags={"XMP:Title": image_title,
                  'XMP:Label': color,
                  'XMP:Creator': 'Eugene Pavlenko'},
            params=["-P", "-overwrite_original"]
        )


def write_data_to_photo_iptc_tools(file):
    with exiftool.ExifToolHelper() as et:
        title = "exiftool"
        et.set_tags(
            [file],
            tags={"XMP:Title": title,
                  "IPTC:ObjectName": title,
                  'XMP:Label': "Green",
                  'XMP:Subject': "keywords/exiftool",
                  'XMP:Description': "caption/exiftool",
                  'XMP:Rating': "3",
                  'XMP:Creator': 'Eugene Pavlenko/exiftool'},
            params=["-P", "-overwrite_original"]
        )

def read_image_metadate(path_to_file):

    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(path_to_file)
        tags = et.get_tags(path_to_file, tags=['XMP:*'])[0]
        tags = et.get_tags([path_to_file], tags=['XMP:Description',
                                                 'XMP:City',
                                                 'XMP:DateCreated',
                                                 'XMP:Urgency',
                                                 'XMP:ColorMode',
                                                 'XMP:CreateDate',
                                                 'XMP:Label',
                                                 'XMP:Rating',
                                                 'XMP:PreservedFileName',
                                                 'XMP:Creator',
                                                 'XMP:Rights',
                                                 'XMP:Subject',
                                                 'XMP:Country',
                                                 'XMP:CountryCode',
                                                 'XMP:Title']
                           )[0]
        # test = et.encoding  # str UTF-8
        # test = et.check_tag_names   # <class 'bool'> True
        # test = et.auto_start   # <class 'bool'> True

        # return metadata[0]
    return tags



if __name__ == '__main__':
    # m_date = read_image_metadate('/Users/evgeniy/Pictures/2023/20230821_недвижимость/20230821EPAV3388.ORF')
    m_date = read_image_metadate('/Users/evgeniy/Downloads/KSP_017764_00642_1h.jpg')
    print(type(m_date))
    print(m_date)
    # pattern = r'(?<=RU ).+(?= Фото:)'
    # print(re.findall(pattern, m_date))
    # for i in m_date.keys():
    #     if i.startswith('EXIF'):
    #         print(i)
    # print(f"{Fore.RED}{m_date.get('XMP:Subject') } ")

    # print(f"{Fore.RED}{m_date.get('IPTC:Caption-Abstract')} ")
    # print(f"{Fore.RED}{m_date.get('EXIF:ImageDescription') } ")
    # print(f"{Fore.RED}{m_date.get('XMP:Description') } ")
    # print()
    # print(f"{Fore.RED}{m_date.get('IPTC:CopyrightNotice')} ")
    # print(f"{Fore.RED}{m_date.get('XMP:Rights') } ")
    # print()
    # print(f"{Fore.RED}{m_date.get('XMP:Credit') } ")
    # print(f"{Fore.RED}{m_date.get('IPTC:Credit')} ")
    # print()
    # print(f"{Fore.RED}{m_date.get('Photoshop:SlicesGroupName') } ")
    # # print(f"{Fore.RED}{m_date.get('IPTC:ExifCameraInfo') } ")
    # print(f"{Fore.RED}{m_date.get('IPTC:ObjectName') } ")



    # for k,v in m_date.items():
    #     print(k,v)






