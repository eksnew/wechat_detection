#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from mmdet.apis import init_detector, inference_detector
import cv2
import store

# 运行命令：python manage.py runserver ip：端口号

def main():

    store.model_rcnn = init_detector(store.config_file_rcnn, store.checkpoint_file_rcnn, device=store.device)
    store.model_detectors = init_detector(store.config_file_detectors, store.checkpoint_file_detectors, device=store.device)
    store.model_yolo = init_detector(store.config_file_yolo, store.checkpoint_file_yolo, device=store.device)

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DIGG.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
