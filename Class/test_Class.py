from importlib import reload
from unittest import TestCase


class ParentClass(TestCase) :
    def __init__ (self) :
        print( "부모 생성자 호출")
    pass 

class LamuneClass(TestCase): # TestCase 는 상속받을 부모 클래스
    """
    __doc__ 정의 : 
    
        __doc__ 에 해당 하는 내용이다. 
        이 객체에 대한 설명
            1. 
            2.
    """
    # 클래스의 string화 시 호출 , 
    # ex) str(new_car) , new_car.__str__() 
    def __str__(self):
        return "This car is SuperCar"

    # 어떤 경우에 호출 되지?
    def __repr__(self):
        return f"<Car '{self._name}'>"


    ## 클래스 Attribute 정의
    #
    _c_attr01 = None # __dict__(X)의 목록에 나오지 않는다.



    ## 생성자
    #
    """
    # 생성자는 한개만 정의 가능 하다.
        *  상속을 사용해도 생성자는 하나의 형태만 사용 가능
    """
    def __init__ (self, name , idd = 0) :
        """
            1. 생성자가 정의되지 않은 경우 부모 생성자 호출 된다.
            2.          정의된 경우 필요하면 부모 생성자를 직접 호출 해야 한다.
        """
        super().__init__()

        # 인스턴스의 내부 Attribute는 어떤 경우든 생성자에서 초기화 or 정의 필요함
        """
            외부 Attribute는 추가적으로 
            get, set의 
        """

        # 인스턴스 Attr 정의 case 01
        self._name = name # __dict__의 목록에 자동으로 보이게 된다.  

        # 인스턴스 Attr 정의 case 02
        self._att_02 = None

        # 인스턴스 Attr 정의 case 03
        self._att_03 = None

    ## 인스턴스 Attr 정의 case 01  (외부 메소드 지원)
    def set_name(self, name ):
        self._name = name


    ## 인스턴스 Attr 정의 case 02 (외부)
    """
        get ,set 으로 접근하는 외부용 property 를 추가로 정의 하는 방식

        __init__ 에서 _att_02  = None 초기화 필요  

        __dict__ 에는 att_02 (X) _att_02 (O) 이 나옴..

        _att_02 , att_02 둘 다 접근 가능
    """ 
    def set_att_02(self, param ):
        self._att_02 = param + 10
    def get_att_02(self):
        return self._att_02 - 5
    att_02 = property ( get_att_02 , set_att_02 ) # 외부 Attr 정의
    
    ## 인스턴스 Attr 정의 case 03 (외부)
    """
        get ,set 이 아닌 직접 attribute에 접근하면 내부 함 수 처리가 동작하는 방식
            att_03 로 접근한 경우에만 프로그램이 동작함

        __init__ 에서 _att_03  = None 초기화 필요  

        __dict__ 에는 att_03 (X) _att_03 (O) 이 나옴..

         _att_03 , att_03 둘 다 접근 가능
    """ 
    @property
    def att_03(self):
        return self._att_03 - 10
    @att_03.setter
    def att_03(self, param):
        self._att_03 = param + 50


    def 부모메소드_호출 ( self ) :
        super().부모메소드()

        
    def test_설명(self) :

        # 클래스 이름 출력
        #__name__ 속성은 클래스를 문자열로 만듭니다.
        print ( f"__name__ = {self.__class__.__name__}" )
         
        # 클래스 설명 출력
        print ( f"__doc__ = {self.__doc__}")

        # 객체의 Attribute , 구현 방법에 따라 누락될 수 있음
        print ( f"__dict__ = {self.__dict__}")

        #`dir()` 함수는 특정 객체의 메소드들을 파악
        print ( f"dir = {dir(self)}" )


        # 내부 _attr_01이 아니라 property 로 정의된 att_01로 접근 하도록 함
        print ( getattr(self, "_att_02") )   # Attribute 접근 case 01
        print ( self._att_02 )   # Attribute 접근 case 02

        return True




    ## 사용될 내부 Custom 예외 정의
    """
    # TypeError 참조
    mro = RuntimeError.mro()
    print( mro[0] ,mro[1] ,mro[2] ,mro[3] )
    <class 'RuntimeError'> <class 'Exception'> <class 'BaseException'> <class 'object'>
    """
    class CustomError(Exception): ...
    class CustomError2(RuntimeError): pass


    def try_사용 (self) :
        try:
            raise self.CustomError("Custom Message")
        
        # cxcept의 순서 주의 : 먼저 해당되는 except만 처리됨
        except self.CustomError as e:
            msg=e.args[0]
            print ( f"CustomError _ {msg}")
        except Exception as e:
            print ( "Exception")
        except RuntimeError as e:
            print ( "RuntimeError")
        else:
            print ( "else")

        finally :
            print ( "fianlly")








#-------------------
    # 참고


"""
# 객체가 인스턴스 인지 확인
 assert True is isinstance(new_car, object)

# 특정 객체의 클래스를 파악
 assert True is (self.Car.__class__ == type)


#파이썬은 클래스에서 다른 클래스가 파생된 경우가 파악
assert True is (issubclass(self.Car, object))
assert True is (issubclass(self.Truck, self.Car))


"""
