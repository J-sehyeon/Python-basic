# 모듈 만들기

# module_basic/

# __name__=="__main__" 
# __name__  / 프로그래밍 언어에서는 프로그램의 진입점을 엔트리 포인트 또는 메인이라고 부른다.   / 이러한 엔트리 포인트 또는 메인  
# 내부에서의 __name__은 "__main__"이다. / 프로그램 진입점은 프로그램 실행 위치를 뜻한다.
# 모듈의 __name__
# module_main/
# __name__ 활용하기 / 엔트리 포인트 파일 내부에서는 __name__이 "__main__"을 출력하므로 이를 사용해 현재 파일이 묘듈로 실행되는지, 
# 엔트리 포인트로 실행되는지 확인할 수 있다.
# module_example/

# 패키지    / 모듈이 모여서 구조를 이룬 것  / pip는 Python Package INdex의 줄임말로 패키지 관리 시스템이다.
# 패키지 만들기
# module_package/
# __init__.py 파일  / 해당 폴더가 패키지임을 알려주고, 패키지와 관련된 초기화 처리를 하는 파일이다.

# 파일은 크게 텍스트 데이터와 바이너리 데이터로 구분된다.
# 텍스트 데이터 / 우리가 쉽게 읽을 수 있는 형태의 데이터이다.
# 바이너리 데이터   / 텍스트 에디터로 열었을 때 의미를 이해할 수 없는 데이터이다.   / 예를들어 100은 바이너리 데이터로 100이라 저장할 수 있다. 
# 이 때 이를 텍스트 에디터로 이를 읽을 경우 100이라는 숫자는 'd'에 해당하여 d가 출력된다. (100을 텍스트 데이터로 저장하면 49 48 48 이다.)
# 바이너리 데이터의 대표적인 예는 이미지와 동영상이다.
# 바이너리 데이터의 장점은 용량이 적다는 것이다.
    # 인코딩과 디코딩   / 사실 텍스트 데이터도, 바이너리 데이터도 2진수의 집합일 뿐이다.
    # 인코딩 방식   / 텍스트 데이터를 맞춰서 우리가 읽기 쉬운 글자로 보여주거나 바이너리 데이터를 이미지로 보여주는 변환 등의 방식을 말한다.    /
    # 예를들어 Python 을 10진수로 표현하면 80 121 116 104 111 110 인 것과 같은 방식이다.
    # 디코딩    / 인코딩된 데이터를 반대로 돌리는 것을 의미한다.
# Chapter07/Chpater07-1/module_urllib.py 에서 urlopen()과 read()함수로 실행한 결과는 단순한 문자열이 아니라 앞에 'b'가 붙어 있다.
# 이는 바이너리 데이터를 의미한다. (바이너리 데이터를 파이썬이 인코딩해서 출력해 주기 때문에 읽을 수 있다.)
# 바이너리 데이터는 문자열(텍스트)가 아니므로 문자열과 관련된 기능(len() 함수 등)을 활용할 수 없다.
# 인터넷의 이미지 저장하기
# binary_download.py

# 모듈 분석
# pip list: 설치된 명령어(모듈) 확인    / pip show 모듈 이름: 모듈의 버전, 위치 등을 알 수 있다.