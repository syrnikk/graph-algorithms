from PIL import Image, ImageDraw, ImageFont
import numpy as np
import math


class GraphVisualizer:
    __img_size = 400
    __padding = 20
    __vertex_radius = 20
    __fi_step = 0.1
    __r = (__img_size - 2 * __padding) / 2
    __img_center = __img_size / 2

    def __init__(self, graph):
        self.__graph_items = graph.items()
        self.__vertex_count = len(self.__graph_items)
        self.__fi = 2 * math.pi / self.__vertex_count
        self.__font = ImageFont.truetype("arial.ttf", self.__vertex_radius)

    def print_to_file(self, file_name):
        image = self.__graph_to_image()
        image.save(file_name)

    def get_image(self):
        return self.__graph_to_image()

    def __graph_to_image(self):
        image = Image.new('RGBA', (self.__img_size, self.__img_size))
        draw = ImageDraw.Draw(image)

        self.__draw_outline_circle(draw)
        self.__draw_edges(draw)
        self.__draw_vertexes(draw)

        return image

    def __draw_outline_circle(self, draw):
        for alpha in np.arange(0.0, 2 * math.pi, self.__fi_step):
            x0 = self.__img_center + self.__r * math.cos(alpha)
            y0 = self.__img_center + self.__r * math.sin(alpha)
            x1 = self.__img_center + self.__r * math.cos(alpha + 0.5 * self.__fi_step)
            y1 = self.__img_center + self.__r * math.sin(alpha + 0.5 * self.__fi_step)
            draw.line([(x0, y0), (x1, y1)], fill=(255, 2, 2))

    def __draw_edges(self, draw):
        pairs = set()

        for key, values in self.__graph_items:
            for value in values:
                pair = frozenset([key, value])
                pairs.add(pair)

        def find_idx(key):
            for i, t in enumerate(self.__graph_items):
                if t[0] == key:
                    return i

        for pair in pairs:
            l = list(pair)
            fr = l[0]
            to = l[1]
            fr_idx = find_idx(fr)
            to_idx = find_idx(to)

            x0 = self.__img_center + self.__r * math.cos(fr_idx * self.__fi - math.pi / 2)
            y0 = self.__img_center + self.__r * math.sin(fr_idx * self.__fi - math.pi / 2)
            x1 = self.__img_center + self.__r * math.cos(to_idx * self.__fi - math.pi / 2)
            y1 = self.__img_center + self.__r * math.sin(to_idx * self.__fi - math.pi / 2)

            draw.line([(x0, y0), (x1, y1)], width=2, fill='black')

    def __draw_vertexes(self, draw):
        for i, key in enumerate(self.__graph_items):
            x0 = self.__img_center + self.__r * math.cos(i * self.__fi - math.pi / 2)
            y0 = self.__img_center + self.__r * math.sin(i * self.__fi - math.pi / 2)

            draw.ellipse((x0 - self.__vertex_radius, y0 - self.__vertex_radius, x0 + self.__vertex_radius,
                          y0 + self.__vertex_radius), fill=(217, 217, 255),
                         outline=(13, 13, 255))

            draw.text((x0, y0), text=str(key[0]), fill='black', font=self.__font, anchor="mm")
