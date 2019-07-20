# Изменение размера изображения

## Описание

Скрипт, который изменяет размер изображения.

## Требования

*Python*

## Как запустить

```sh
git clone https://github.com/Safintim/12_image_resize.git
cd 12_image_resize
pip install -r requirements.txt
python image_resize.py --image <path_to_image> <other_args>
```

## Возможные аргументы
```sh
--image  # (-i) путь к изображению. Единственный обязательный. 
--scale  # (-s) масштаб.
--width  # (-wt) ширина.
--height # (-ht) высота.
--output # (-o) Куда класть результирующий файл. По умолчанию сохраняет в директорию с расположением скрипта в таком виде: imagename_200x400.jpeg.
--help   # (-h) справка
```

## Примеры запуска скрипта

```sh
python image_resize.py --image test.jpeg  --width 200 --output new_image.jpeg
```

```sh
python image_resize.py --image test.jpeg  --width 200 --height 300 --output new_image.jpeg
Proportion do not match
```

```sh
python image_resize.py --image test.jpeg  --scale 2 --output new_image.jpeg
```

```sh
python image_resize.py --image test.jpeg  --scale 2 --width 200 --height 300 --output new_image.jpeg
ValueError: You cannot scale the image when the dimensions are specified
```

## Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
