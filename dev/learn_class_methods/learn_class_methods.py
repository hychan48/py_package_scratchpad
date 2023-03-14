import logging as log
from stringcolor import cs
import pytest
import sys


# to look at... abstractmethods / interfaces in python 3
# https://docs.python.org/3/library/abc.html
# there are custom libs...
# https://stackoverflow.com/questions/2124190/how-do-i-implement-interfaces-in-python
# seems like in python, just overkill
# but there's @property as well
# that's what im looking for
# metaclass...

# not really a class. more like a factory function
class CustomLogger:
    """
    Let's say i want to take specifc parameters a,b
    one class i want to use print, and in another i want to use logging
    """
    str_to_append = "CL: "
    cl_to_append = 'blue'

    # tmp = str(cs(str_to_append, cl_to_append)) # not needed anymore? or make static
    # might need to make a metaclass or do this in __init__ + class method?

    @classmethod
    # def init_metadata(cls, str_to_append:str = "CL: ", cl_to_append:str = 'blue'):
    def init_metadata(cls, str_to_append: str = None, cl_to_append: str = None):
        """
        fake metaclass?
        kinda lame... can't set variables like this
        :return:
        """
        d_locals = locals()
        for arg in ("str_to_append", "cl_to_append"):  # should refactor a private version of this
            # so dont need to check for None
            if d_locals[arg] is not None:
                # cls[arg] = d_locals[arg]
                setattr(cls, arg, d_locals[arg])
        setattr(cls, 'tmp', str(cs(cls.str_to_append, cls.cl_to_append)))
        return cls
        # return cls() # what's the difference?, this will crash though
        # return str(cs(cls.str_to_append,'blue'))

    def __init__(self,cl_to_append=None,str_to_append=None):
        # these are class properties. so that's why there's no params in init
        self.init_metadata(str_to_append, cl_to_append)

    @classmethod  # this works but kinda meaning less
    # guess i should be doing them inside __init__ instead like in init_metadata
    # @deprecated
    def change_color(cls, color):
        """
        Class methods are like custom init / constructors. but class level
        creates pseudo children classes
        doesn't work too well though
        :return:
        """
        cls.cl_to_append = color
        cls.tmp = str(cs(cls.str_to_append, cls.cl_to_append))
        return cls
    # is this also more of a class method than anything? since it's static
    @classmethod
    def log(cls, s_input: str):
    # def log(self, s_input: str):
        # log.warning(f"{self.str_to_append}{s_input}")
        # log.warning(f"{self.tmp}{s_input}")
        log.warning(f"{cls.tmp}{s_input}")


class WhiteInfoLogger(CustomLogger):
    """
        Simple override... easier than using classmethod imo
    """
    str_to_append = "WIL: "
    cl_to_append = 'white'
    # @classmethod
    # def init_cs(cls):
    #     cls.tmp = str(cs(cls.str_to_append, cls.cl_to_append))  # still need this though
    # init_cs()
    # good place to use classmethod. nope. probably static one instead


# PyTest

def test_name():
    """
    @classmethod does not produce factory functions as expected...
    seems like it's just for storing static data amongst the classes
    :return:
    """
    cl = CustomLogger()
    cl.log('blue CL')

    cl_red = CustomLogger().change_color('red')
    cl_red.log('red CL')

    cl_white = WhiteInfoLogger()
    cl_white.log('white wil')
    cl_red.log('red CL')
    cl.log('blue CL got changed...') # so it's not really a factory function
    # it's really just static. but at least the init is nice?
    cls_meta = CustomLogger.init_metadata()()
    cls_meta.log('blue CLS')
    cl_red.log('red CL - init _metadata_broke red color') # init metadata broke it
    # repeating to see if anything broke
    cl.log('blue CL')
    cl_red.log('red CL') # this broke... probably because i didnt call it right
    cl_white.log('white wil')
    cls_meta.log('blue CLS')

def test_name_init_only():
    cl = CustomLogger()
    cl.log('blue CL')

    cl_red = CustomLogger('red')
    cl_red.log('red CL')

    cl_white = WhiteInfoLogger()
    cl_white.log('white wil')
    cl_red.log('red CL')
    cl.log('blue CL got changed...') # so it's not really a factory function
    # it's really just static. but at least the init is nice?
    cls_meta = CustomLogger('yellow')
    cls_meta.log('yellow CLS')
    cl_red.log('red CL - init _metadata_broke red color') # init metadata broke it
    # repeating to see if anything broke
    cl.log('blue CL')
    cl_red.log('red CL') # this broke... probably because i didnt call it right
    cl_white.log('white wil')
    cls_meta.log('yellow CLS')




if __name__ == '__main__':
    pytest.main(sys.argv)
