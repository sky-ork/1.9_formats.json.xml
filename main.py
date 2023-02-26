import json
import xml.etree.ElementTree as ET


def get_in_json_list_words(filename):
    data = {}
    words_list = []
    with open(filename, encoding='UTF-8') as f:
        data.update(json.load(f))
    for item in data['rss']['channel']['items']:
        words_list.extend(str(item['description']).lower().split())
        words_list = [word for word in words_list if len(word) > 6]
    return words_list


def get_in_xml_list_words(filename):
    words_list = []
    parser = ET.XMLParser(encoding='UTF-8')
    tree = ET.parse(filename, parser)
    root = tree.getroot()
    data = root.findall('channel/item')
    for item in data:
        words_list.extend(str(item.find('description').text).lower().split())
        words_list = [word for word in words_list if len(word) > 6]
    return words_list


def get_top_words(words_list):
    word_count = {}
    for word in words_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    sorted_words = sorted(word_count.items(), key=lambda i: i[1], reverse=True)
    top_words = sorted_words[:10]
    return top_words


def main():
    list_words_json = get_in_json_list_words('files/newsafr.json')
    top_words_json = get_top_words(list_words_json)
    print('Топ 10 слов в файле newsafr.json:')
    for numb, top in enumerate(top_words_json, 1):
        print(str(numb) + '.', top[0], '-', top[1])

    print()

    list_words_xml = get_in_xml_list_words('files/newsafr.xml')
    top_words_xml = get_top_words(list_words_xml)
    print('Топ 10 слов в файле newsafr.xml:')
    for numb, top in enumerate(top_words_xml, 1):
        print(str(numb) + '.', top[0], '-', top[1])


if __name__ == '__main__':
    main()
