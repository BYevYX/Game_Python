"""
Module: game.src.image_cache

This module defines a static class `ImageCache` for caching and retrieving images,
with optional scaling based on screen scaling factors.

Attributes:
- cache (dict): A dictionary to store loaded images keyed by their file paths.

Methods:
- get_images(paths, scale=None):
    Load images from specified paths and optionally scale them based on provided scaling factors.
    If no scaling factors are provided, default screen scaling factors are used.

Usage:
images = ImageCache.get_images(["path/to/image.png", "path/to/another/image.png"], (2, 2))

This class is useful for efficiently loading and managing images in a game, ensuring that
images are loaded only once and optionally scaled to match the current screen resolution.

Example:
    from game.src.image_cache import ImageCache
    import pygame

    # Example usage to load and scale images
    images = ImageCache.get_images(["path/to/image.png", "path/to/another/image.png"], (2, 2))

Notes:
- Ensure that `screen_obj` from `game.src.screen` is correctly initialized before using this module,
  as it is used for scaling images based on screen dimensions.

"""
from game.src.screen import screen_obj
import pygame


class ImageCache:
    """
        A static class to cache and retrieve images,
        optionally scaled based on screen scaling factors.

        Attributes:
            cache (dict): A dictionary to store loaded images keyed by their file paths.

        Methods:
            get_images(paths, scale=None):
                Load images from specified paths and scale them if required.

        Usage:
            images = ImageCache.get_images(["path/to/image.png",
                                            "path/to/another/image.png"], (2, 2))
        """

    cache = {}

    @staticmethod
    def get_images(paths, scale=None):
        """
        Load and return a list of images from the specified paths, optionally scaling them.
        :param paths: list of file paths for the images.
        :param scale: Tuple (width_scale, height_scale) for scaling the images.
        If None, default scaling is used.
        :rtype: list
        :return: loaded and scaled images.
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
