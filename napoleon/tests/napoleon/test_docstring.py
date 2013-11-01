# -*- coding: utf-8 -*-
# Copyright 2013 Rob Ruana
# Licensed under the BSD License, see LICENSE file for details.

"""Tests for :mod:`sphinxcontrib.napoleon.docstring` module."""

import textwrap
from sphinxcontrib.napoleon.docstring import GoogleDocstring, NumpyDocstring
from unittest import TestCase


class BaseDocstringTest(TestCase):
    pass


class GoogleDocstringTest(BaseDocstringTest):
    docstrings = [(
        """Single line summary""",
        """Single line summary"""
    ), (
        """
        Single line summary

        Extended description

        """,
        """
        Single line summary

        Extended description
        """
    ), (
        """
        Single line summary

        Args:
          arg1(str):Extended
            description of arg1
        """,
        """
        Single line summary

        :Parameters: **arg1** (*str*) --
                     Extended
                     description of arg1"""
    ), (
        """
        Single line summary

        Args:
          arg1(str):Extended
            description of arg1
          arg2 ( int ) : Extended
            description of arg2

        Keyword Args:
          kwarg1(str):Extended
            description of kwarg1
          kwarg2 ( int ) : Extended
            description of kwarg2""",
        """
        Single line summary

        :Parameters: * **arg1** (*str*) --
                       Extended
                       description of arg1
                     * **arg2** (*int*) --
                       Extended
                       description of arg2

        :Keyword Arguments: * **kwarg1** (*str*) --
                              Extended
                              description of kwarg1
                            * **kwarg2** (*int*) --
                              Extended
                              description of kwarg2"""
    ), (
        """
        Single line summary

        Arguments:
          arg1(str):Extended
            description of arg1
          arg2 ( int ) : Extended
            description of arg2

        Keyword Arguments:
          kwarg1(str):Extended
            description of kwarg1
          kwarg2 ( int ) : Extended
            description of kwarg2""",
        """
        Single line summary

        :Parameters: * **arg1** (*str*) --
                       Extended
                       description of arg1
                     * **arg2** (*int*) --
                       Extended
                       description of arg2

        :Keyword Arguments: * **kwarg1** (*str*) --
                              Extended
                              description of kwarg1
                            * **kwarg2** (*int*) --
                              Extended
                              description of kwarg2"""
    ), (
        """
        Single line summary

        Return:
          str:Extended
          description of return value
        """,
        """
        Single line summary

        :returns: *str* --
                  Extended
                  description of return value"""
    ), (
        """
        Single line summary

        Returns:
          str:Extended
          description of return value
        """,
        """
        Single line summary

        :returns: *str* --
                  Extended
                  description of return value"""
    )]

    def test_docstrings(self):
        for docstring, expected in self.docstrings:
            actual = str(GoogleDocstring(textwrap.dedent(docstring)))
            expected = textwrap.dedent(expected)
            self.assertEqual(expected, actual)


class NumpyDocstringTest(BaseDocstringTest):
    docstrings = [(
        """Single line summary""",
        """Single line summary"""
    ), (
        """
        Single line summary

        Extended description

        """,
        """
        Single line summary

        Extended description
        """
    ), (
        """
        Single line summary

        Parameters
        ----------
        arg1:str
            Extended
            description of arg1
        """,
        """
        Single line summary

        :Parameters: **arg1** (*str*) --
                     Extended
                     description of arg1"""
    ), (
        """
        Single line summary

        Parameters
        ----------
        arg1:str
            Extended
            description of arg1
        arg2 : int
            Extended
            description of arg2

        Keyword Arguments
        -----------------
          kwarg1:str
              Extended
              description of kwarg1
          kwarg2 : int
              Extended
              description of kwarg2
        """,
        """
        Single line summary

        :Parameters: * **arg1** (*str*) --
                       Extended
                       description of arg1
                     * **arg2** (*int*) --
                       Extended
                       description of arg2

        :Keyword Arguments: * **kwarg1** (*str*) --
                              Extended
                              description of kwarg1
                            * **kwarg2** (*int*) --
                              Extended
                              description of kwarg2"""
    ), (
        """
        Single line summary

        Return
        ------
        str
            Extended
            description of return value
        """,
        """
        Single line summary

        :returns: *str* --
                  Extended
                  description of return value"""
    ), (
        """
        Single line summary

        Returns
        -------
        str
            Extended
            description of return value
        """,
        """
        Single line summary

        :returns: *str* --
                  Extended
                  description of return value"""
    )]

    def test_docstrings(self):
        for docstring, expected in self.docstrings:
            actual = str(NumpyDocstring(textwrap.dedent(docstring)))
            expected = textwrap.dedent(expected)
            self.assertEqual(expected, actual)
