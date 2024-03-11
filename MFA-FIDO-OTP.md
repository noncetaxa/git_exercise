

# 2차 인증

1차 인증(username + password)에 더해 다른 요소 1가지를 더해 인증하는 것을 '2 요소 인증(Two-Factor Authentication)' 또는 '이중 인증'이라고 함 -> 아랫쪽 FIDO U2F 참고



## 국내 3대 컴플라이언스 요구 주체

1. 행정안전부(지자체)
2. 금융보안(연구)원(금융권)
3. 국정원(기타)



## 다중 요소 인증 Multi Factor Authentication(MFA)

- 이중 인증의 확장 개념

    - ['접근 권한 관리의 기본' MFA 솔루션 제대로 고르기 - ITWorld Korea](https://www.itworld.co.kr/news/260914)

- MFA의 종류

    - **One-Time Password(OTP)** 

        - = One Time Authorization Code(OTAC) = dynamic password
        - 원리: [일회용 암호, OTP의 원리는? – Sciencetimes](https://www.sciencetimes.co.kr/news/일회용-암호-otp의-원리는/)

    - 생체인증

        - 지문, 홍채, 얼굴 등을 인식해 인증하는 방식

        - 생체 인증 자체는 오프라인에서 사용되어 왔던 기술

        - **온라인 환경에서 2차 인증에 응용되도록 한 것이 FIDO**

    - SMS/메신저

    - QR



# Fast IDentity Online(FIDO)

- 참고

    - 요약: [비밀번호 사용을 줄이기 위한 'FIDO'의 의미와 인증 프로세스 - ITWorld Korea](https://www.itworld.co.kr/news/181859)
    - 역사: ["비밀번호 없는 미래를 계획한다"...국제온라인인증연합 - ITWorld Korea](https://www.itworld.co.kr/tags/65283/FIDO/90956)
- 공개키 암호화가 기반 규약

    - [Public key infrastructure - Wikipedia](https://en.wikipedia.org/wiki/Public_key_infrastructure)
    - 암호화에는 공개키, 복호화에는 개인키 사용
    - SSL/TLS과 **PKI**(Public Key Infrastructure)의 기반
    - 대표적 알고리즘은 RSA (SSH 접속시 흔히 사용)
- 인증이 로컬 기기 내에서 일어나고 그 결과만 내보낸다는 점이 핵심

    - 인증 데이터를 그대로 서버에 전송하는 방식 X
    - 사용자의 인증장치를 통한 인증 결과 값을 암호화해 서버로 전송
    - 이를 서버에서 받아 복호화 해 검증



## FIDO alliance(보안산업계 국제 연합)

- [FIDO Alliance Overview - Changing the Nature of Authentication](https://fidoalliance.org/overview/)

    - 인증 표준의 개발: 인증 및 기기 증명에 대한 표준의 개발, 사용 및 준수 촉진, 관리

    - 삼성전자도 컨소시엄 참여중(구글, MS, 아마존, 페이팔 등)

    - "FIDO 얼라이언스는 다음과 같은 방법으로 사명을 완수하기 위해 노력합니다."

        - *사용자를 인증하기 위해 **암호에 대한 의존도를 줄이는** 개방적이고 확장 가능하며 **상호 운용 가능한 메커니즘 집합**을 정의하는 기술 사양 개발*

        - *공식 표준화를 위해 공인된 표준 개발 조직에 성숙한 기술 사양 제출*

        - *전 세계적으로 사양을 성공적으로 채택할 수 있도록 **업계 인증 프로그램**을 운영합니다.*

    ### FIDO Certification

    - 인증 회사, 규약, 버전, 유형 등 검색:  https://fidoalliance.org/certification/fido-certified-products/
    - 미래 테크놀로지(한국정보인증) [KICA - 한국정보인증 (mirae-tech.co.kr)](http://www.mirae-tech.co.kr/miraetech/platform/introduce.jsp)
    - 한국전자인증 https://solution.crosscert.com/bio/fido/



## 1. FIDO

- ### UAF(Universal Authentication Framework)

    - 모바일 기기 인증에 특화
    - 기기에 계정을 등록(PIN, 지문, 얼굴 등)
    - 인증을 할 때는 서비스 제공업체와 인증 결과(암호화된)를 교환
    - 인증 데이터 자체는 서비스 제공업체에서 볼 수 없음

- ### U2F(Universal *Second Factor*)

    - *2차 인증*으로서 비밀번호 인증 보완하는 **물리키** 사용
    - 구글이 내부용으로 만들기 시작: https://store.google.com/us/product/titan_security_key?hl=en-US
    - FIDO alliance가 관리권한 가지는 **전용 하드웨어** 사용



## 2. FIDO2

1. ### [WebAuthn(웹인증)](https://webauthn.guide/)

    - **API로 구현**: 모바일 기기 외에도 브라우저(PC 등)에서도 로컬 인증이 가능하도록

2. Client to Authenticator Protocols(CTAP)

    - 서비스업체 **<= '별도 인증 플랫폼에서 웹인증' =>** 사용자 PC
    - **CTAP1**:  U2F 개정판(웹인증에 물리적 전자 열쇠 사용)
    - **CTAP2**: CTAP1의 확장(무선랜, 블루투스, USB 등으로 모바일/웨어러블 기기 사용해 인증)
    - digital signature: 신원 증명용으로 양식화된 데이터를 암호화한 것



## 3. Passkey 

- [구글·애플·마이크로소프트 손잡고 패스워드 없는 시대 간다](https://zdnet.co.kr/view/?no=20221220163938)
    - 사용자가 서비스마다 개별 기기를 등록해야 하는 방식에서 벗어남
    - **클라우드 동기화**를 통해 자동으로 로그인이 되기 때문에 여러 기기에 로그인 서비스를 각각 등록할 필요가 없는 것이 특징
    - 클라우드에서 개인키가 안전하게 암호화돼 동기화(**WebAuthn API 이용)**
    - 마이크로소프트, 구글, 애플 3사 제공(2022년 12월 기준)
- [애플의 FIDO 얼라이언스 합류 및 확장](https://www.wired.kr/news/articleView.html?idxno=4194)



# OTP

- 개요: [OTP(일회용 비밀번호): 정의, 모범 사례 및 예 (entrust.com)](https://www.entrust.com/ko/resources/faq/what-is-a-one-time-password)
- 특징: 암호가 일정한 시간마다 바뀜 -> 지식 기반이 될 수 없음

## OTP의 형태: 기본적으로 소유 기반 인증임

- 하드 토큰: 물리기기. 카드형, USB형([Yubikey](https://www.yubico.com/products/)) 등 
    - 분실 도난 훼손 가능성 있음
- 소프트 토큰: 소프트웨어로 구현 
    - 후킹, 라우팅 가능성 있음
- SMS/전화(ARS)/메일/기타 프로그램이나 인증 방식
    - 단, SMS OTP는 FIDO 얼라이언스에 의해 지양되고 있다. ("FIDO 얼라이언스는 비밀번호 및 SMS OTP보다 더 안전하고, 소비자가 사용하기 쉽고, 서비스 제공업체가 더 쉽게 배포하고 관리할 수 있는 개방형 표준으로 인증의 특성을 바꾸기 위해 노력하고 있습니다.")
- OTP 숫자가 인쇄된 카드나 종이 등



## OPT의 토큰 발행 방식

### 1. 시간 동기화: Time-based OTP(TOTP)

- 인증 서버와 동기화된 시계가 내장된 토큰을 이용
- OTP 버튼이 있어 누르면 시간과 고유번호를 seed로 해 알고리즘을 통해 임의의 숫자가 발생된다.
- 그리핀 타워의 OTP 6자리 생성에는 **HMAC SHA-1** 알고리즘 사용(하단 설명 참고)
    - HMAC? H + MAC = Hash-based + Message Authentication Code
    - 즉, 키 있는 해시 함수(Keyed Hash Function) 종류 중, 대표적인 '메시지 인증 코드'(message authentication code, MAC).
    - '메시지 인증 코드'는 **대칭키** 암호화
- QR코드와 함께 사용됨


### 2. 이벤트 동기화: Hash Chain/해시 기반 OTP(HOTP)

해시 알고리즘 **비대칭키** 암호화 방식으로, 복호화가 어려운 특징을 활용

참고: [One Time Password(OTP)의 개념 및 동작방식. LDAP을 활용한 OTP 인증. - DSMENTORING](https://ldap.or.kr/1373-2/)



### 3. 비동기화: Challenge - Response (질의 응답)

1. 사용자가 인증서버로 로그인 시도
2. 서버에서 사용자에게 질의 값 보냄
3. 사용자가 서버에 응답 값 생성 후 보냄
4. 서버가 응답 값을 비교해 인증함



### 4. S/Key: 벨 통신 연구소에서 개발해 유닉스 환경에서 사용

- 사용자가 소프트웨어를 설치해서 사용
- 사용자가 임의의 값을 서버로 보내면 이를 해싱하고 그 값을 계속 연쇄 해싱한 값을 저장해서 사용


---

### HMAC SHA1 알고리즘

HMAC SHA1는 SHA1 해시 함수에서 생성되고 HMAC 또는 해시 기반 메시지 인증 코드로 사용되는 키 지정 해시 알고리즘 유형입니다. HMAC 프로세스는 비밀 키와 메시지 데이터를 혼합하고, 해시 함수로 결과를 해시하고, 해당 해시 값을 비밀 키와 다시 혼합한 다음, 해시 함수를 두 번째로 적용합니다. 출력 해시의 길이는 160비트입니다.

HMAC는 보낸 사람과 받는 사람이 비밀 키를 공유하는 경우 안전하지 않은 채널을 통해 보낸 메시지가 변조되었는지 여부를 확인하는 데 사용할 수 있습니다. 발신자는 원래 데이터의 해시 값을 계산하고 원본 데이터와 해시 값을 모두 단일 메시지로 보냅니다. 수신자는 수신된 메시지의 해시 값을 다시 계산하고 계산된 HMAC가 전송된 HMAC와 일치하는지 확인합니다.

데이터 또는 해시 값을 변경하면 메시지를 변경하고 올바른 해시 값을 재현하려면 비밀 키에 대한 지식이 필요하기 때문에 불일치가 발생합니다. 따라서 원래 해시 값과 계산된 해시 값이 일치하면 메시지가 인증됩니다.

SHA-1(Secure Hash Algorithm, SHS, Secure Hash Standard라고도 함)은 미국 정부에서 발표한 암호화 해시 알고리즘입니다. 임의의 길이 문자열에서 160비트 해시 값을 생성합니다.

HMAC SHA1는 모든 크기의 키를 허용하며 길이가 160비트인 해시 시퀀스를 생성합니다.

SHA1과의 충돌 문제로 인해 SHA256을 사용하는 것이 좋습니다.

---



# 미래 테크놀로지(현 한국정보인증)의 여러 문서에서 쓰이는 "OTP 키"라는 표현이 가리키는 것은 정확히 무엇인가?

"OTP 키" = "S/W OTP 인증키" = "OTP 비밀키" = "OTP Key" = "공유비밀키"

- OTP의 이 키 자체는 비대칭 키가 아님(공개-개인키 사용 X)
- PC 또는 모바일용 S/W로 구현된 OTP 토큰(개별 기기 상의 mOTP)에 부여되는 고유값을 의미
