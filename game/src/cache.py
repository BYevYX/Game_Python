import pygame

from game.src.screen import screen_obj


class ImageCache:
    cache = {}

    @staticmethod
    def get_images(paths, scale=None):
        """

        :rtype: list
        :param paths:
        :param scale:
        :return:
        """
        images = []
        for path in paths:
            if path not in ImageCache.cache:
                ImageCache.cache[path] = pygame.image.load(path).convert_alpha()

            if scale:
                images.append(pygame.transform.scale(ImageCache.cache[path],
                                                     (ImageCache.cache[path].get_width() * scale[
                                                         0] * screen_obj.width_scale,
                                                      ImageCache.cache[path].get_height() * scale[
                                                          1] * screen_obj.height_scale)))
            else:
                images.append(pygame.transform.scale(ImageCache.cache[path],
                                                     (ImageCache.cache[path].get_width() * screen_obj.width_scale,
                                                      ImageCache.cache[path].get_height() * screen_obj.height_scale)))
        return images
