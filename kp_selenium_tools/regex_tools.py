import re

from kp_selenium_tools.bad_words_job import get_bad_words_from_txt_file


def get_file_extension(path_to_file: str) -> str:
    # re_pattern = r'(?<=\.)[1A-Za-z_]{3,8}'  # work correctly with only one dot in filename
    re_pattern = r'(?<=\.)[^.]+$'
    extension = re.findall(re_pattern, path_to_file)[0]
    return extension  # string with file extension


def get_file_name_no_extension(file_name: str):
    rg_pattern = r'[^.]+(?=\.)'
    # didn't work with hidden files
    file_name_no_extension = re.findall(rg_pattern, file_name)
    if len(file_name_no_extension) != 0:
        return file_name_no_extension[0]


def extract_only_words(text_string):
    if type(text_string) is list:
        text_string = ''.join(text_string)
    pattern = r'[А-Яа-яA-Za-z]+\-*[А-Яа-яA-Za-z]+'
    return re.findall(pattern, text_string)


def extract_words_no_digits(text_string):
    if type(text_string) is list:
        text_string = ''.join(text_string)
    pattern = r'[А-Яа-яA-Za-z]+\-*[А-Яа-яA-Za-z]+'
    return re.findall(pattern, text_string)


def modify_caption(image_metadata):
    try:
        caption = image_metadata['XMP:Description'].replace('\n', ' ')
        pattern = r'(?<=RU ).+(?= Фото:)'
        if len(re.findall(pattern, caption)) != 0:
            image_metadata['XMP:Description'] = re.findall(pattern, caption)[0]
    except KeyError as e:
        print(e)
    return image_metadata


def keywords_opimization(string):
    words_to_remove = get_bad_words_from_txt_file('/Users/evgeniy/Documents/keywords/bad_words.txt')

    # remove bad words
    no_bad_words = re.sub(words_to_remove, "", string).strip()

    # remove doubles
    cleaned_string = re.sub(r'\b(\w+)\b(?=.*\b\1\b)', r'', no_bad_words)

    # Remove all punctuation except commas
    cleaned_string = re.sub(r'(?<!\w)[^\w\s,-]|[^\w\s,-](?!\w)', '', cleaned_string)

    # Extract words and separate with commas
    words = re.findall(r'\b[\w-]+\b', cleaned_string)
    result = ', '.join(words)

    # set limit of keywords
    while len(result) > 500:
        del words[-1]
        result = ', '.join(words)

    return result


def replace_to_comma(keywords: str) -> str:
    words_to_remove = get_bad_words_from_txt_file('/Users/evgeniy/Documents/keywords/bad_words.txt')
    step_1 = re.sub(words_to_remove, '', keywords).strip()  # remove this words
    return re.sub(r';', ', ', step_1)


def create_add_image_link(shoot_id: str, count: int) -> str:
    #  Создаю ссылку окна браузера добавление снимки в архив
    count_str = str(count).zfill(5)
    return f'https://image.kommersant.ru/photo/wp/AddPhotoTask.aspx?photocode=' \
           f'{shoot_id}_{count_str}&filename={shoot_id}_{count_str}'


def make_text_edit_link(link):
    inner_id = re.findall(r'(?<=id=)\d+', link)[0]
    image_id = re.findall(r'(?<=photocode=)[^&]+', link)[0]
    # image_edit_link = f'https://image.kommersant.ru/photo/archive/ViewPhoto.asp?ID={inner_id}&Lang=1&L=1'
    image_edit_link = f'https://image.kommersant.ru/photo/archive/adm/AddPhotoStep3.asp?ID={inner_id}&CloseForm=1'
    return image_edit_link, image_id, inner_id


def make_preview_photo_link(link):
    inner_id = re.findall(r'(?<=id=)\d+', link)[0]
    image_id = re.findall(r'(?<=photocode=)[^&]+', link)[0]
    image_edit_link = f'https://image.kommersant.ru/photo/archive/ViewPhoto.asp?ID={inner_id}&Lang=1&L=1'
    return image_edit_link, image_id, inner_id


def full_shoot_html_link(shoot_id: str, page: int) -> str:
    # create full shoot html link with 200 preview (Так называемый "просмотр съемки")
    splited_soot_id = shoot_id.split('_')
    return f'https://image.kommersant.ru/photo/wp/default.aspx?shootnum={splited_soot_id[1]}' \
           f'&sourcecode={splited_soot_id[0]}&pagesize=200&previewsize=128&page={str(page)}&nl=true&ord=F'


if __name__ == '__main__':
    assert type(full_shoot_html_link('KSP_017605', 0)) == str
    # print(f"{'replace_to_comma'}: {replace_to_comma('Санкт - Петербург, Петрикирхе;архитектура;религия,религия ')}")
    # print(
    #     f"{'keywords_opimization'}: "
    #     f"{keywords_opimization('Санкт-Петербург, Петрикирхе;архитектура;религия, архитектура')}")
    #
    # print(full_shoot_html_link('KSP_017945', 1))

    assert type(get_file_name_no_extension('KSP_017547_00011_1h.jpg')) == str
    assert len(get_file_name_no_extension('KSP_017547_00011_1h.jpg')) != 0
    assert get_file_name_no_extension('.DS_store') is None
    assert get_file_name_no_extension('KSP_017547_00011_1h.jpg') == 'KSP_017547_00011_1h'
    assert get_file_extension('2023-02-28_20-23-08_report.pdf') == 'pdf'
    assert get_file_extension('.DS_store') == 'DS_store'
    assert get_file_extension('20231006EPAV2441.ORF.dop') == 'dop'
