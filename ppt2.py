import streamlit as st
import pydeck as pdk
import folium
from streamlit_folium import st_folium
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import datetime

import subprocess
import sys
from streamlit_google_auth import Authenticate

# Set page configuration
st.set_page_config(page_title="My App", layout="wide")

# 인증 객체 생성
authenticator = Authenticate(
    secret_credentials_path=r"C:\Users\USER\Desktop\presentation\client_secret_627605090023-9l103ck2gmqeicd67vu2824e8tuov5r5.apps.googleusercontent.com.json",
    cookie_name='your_cookie_name',
    cookie_key='your_cookie_key',
    redirect_uri='http://localhost:8501',
)

# 인증 상태 확인
authenticator.check_authentification()

if not st.session_state.get('connected'):
    # 로그인 버튼 표시
    authenticator.login()
else:
    # 사용자 정보 표시 및 로그아웃 버튼
    st.image(st.session_state['user_info'].get('picture'))
    st.write(f"안녕하세요, {st.session_state['user_info'].get('name')}님!")
    st.write(f"이메일: {st.session_state['user_info'].get('email')}")
    if st.button('로그아웃'):
        authenticator.logout()
        
# yfinance 설치
#try:
#    import yfinance as yf
#except ImportError:
#    subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])
#    import yfinance as yf


#import yfinance as yf



# Define menu items
brands = ["UNIQLO", "ZARA", "GAP"]
sub_menus = ["기업개요", "연혁", "재무", "비즈니스 분석", "AI전략", "결론"]

# Sidebar styling with CSS
st.markdown("""
    <style>
    /* Main page background */
    .main {
        background-color: #f0f2f6;
        padding-top: 20px;
        padding-bottom: 20px;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #2c3e50;
        color: #ecf0f1;
        font-size: 18px;
    }

    [data-testid="stSidebar"] h1 {
        color: #ecf0f1;
        font-weight: bold;
        font-size: 24px;
    }

    /* Sidebar selection box styling */
    .st-cp {
        background-color: #34495e;
        border-radius: 5px;
        padding: 8px;
    }
    
    .st-cp select {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for brand selection
st.sidebar.title("Contents")
selected_brand = st.sidebar.selectbox("Enterprises", ["MAIN"] + brands)  # Add default "MAIN" option

# Sidebar for sub-menu selection (only show if a brand is selected)
if selected_brand != "MAIN":
    selected_sub_menu = st.sidebar.selectbox("Index", ["MAIN"] + sub_menus)
else:
    selected_sub_menu = "MAIN"

# Show main page content only if no brand or sub-menu is selected
if selected_brand == "MAIN" or selected_sub_menu == "MAIN":
    # Main page content with background color
    st.markdown("""
        <div style="text-align: center; font-size: 40px; font-weight: bold; color: #2c3e50; margin-bottom: 20px;">
            Presentation about Fashion Enterprises
        </div>
        <div style="text-align: center; font-size: 30px; font-weight: bold; color: #7f8c8d; margin-bottom: 40px;">
            -UNIQLO, ZARA, GAP-
        </div>
        <div style="text-align: right; font-size: 24px; font-weight: bold; color: #34495e;">
            -경훈)-
        </div>
    """, unsafe_allow_html=True)

    # Central image
    st.image(
        r"C:\Users\USER\Desktop\presentation\메인.webp",
        use_column_width=True
    )
else:
    # Display content based on selected brand and sub-menu
    ## st.title(f"{selected_brand} - {selected_sub_menu}")
        # Display selected brand and sub-menu with customized styling

        #<div style="font-size: 30px; font-weight: bold; margin-top: 5px;">{selected_sub_menu}</div>
    st.markdown(f"""
        <div style="text-align: left;">
            <div style="font-size: 40px; font-weight: bold;">{selected_brand}</div>
            
        </div>
    """, unsafe_allow_html=True)

    if selected_brand == "UNIQLO":
        if selected_sub_menu == "기업개요":
            st.title("Fast Retailing")

            # 좌우 레이아웃 구성
            col1, col2 = st.columns([1, 2])

            # 왼쪽에 로고 표시
            with col1:
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/FAST_RETAILING_logo.svg/225px-FAST_RETAILING_logo.svg.png", caption="Fast Retailing", use_column_width=True)
                st.image("https://www.fastretailing.com/eng/group/images/default.jpg", caption="주요 브랜드", use_column_width=True)

            # 오른쪽에 기업 정보 요약
            with col2:
                st.subheader("기업 개요")
                st.markdown("""    
                <span style="font-size:23px;">
                
                - **설립** : 1965년 (당시 명칭: 오고리상사)  \n
                - **본사 위치** : 일본 야마구치현 야마구치시  \n
                - **CEO** : 야나이 타다시 (Tadashi Yanai)  \n
                - **주요 브랜드** : 유니클로(UNIQLO), GU, Theory 등
                </span>
                """,  unsafe_allow_html=True)

                st.subheader("사업 규모")
                st.markdown("""
                <span style="font-size:50px;">
                            
                - **2024년 연간 매출** : 3조 1,038억 엔  \n
                - **유니클로 매출** : 2조 6,440억 엔 (전체 매출의 약 85%)  \n
                - **전 세계 유니클로 매장 수** : 2,495개
                </span>
                """,  unsafe_allow_html=True)


            st.markdown(    """
    - 모기업은 FastRetailing. 유니클로가 전체 모기업 매출의 84% 차지. 일본의 대표적인 의류 브랜드로, 주로 기본 스타일과 실용적인 디자인을 중심으로 다양한 연령층에 맞춘 패션을 제공.
    - 유니크(Unique)와 의류(Clothing)의 합성어, 합리적인 가격과 고품질을 겸비한 일상 패션 추구
    - SPA(제조·유통 일괄형) 모델, LifeWear(유행을 잘 타지 않는), 기술혁신([히트텍](https://www.hankyung.com/article/2024100674311), [에어리즘](https://www.wolyo.co.kr/news/articleView.html?idxno=238275)), 글로벌 확장 및 지속 가능성
    """
)

            # 브랜드 소개 데이터
            data = {
                "브랜드": ["GU", "Theory", "PLST", "COMPTOIR DES COTONNIERS", "Princess tam.tam"],
                "규모" : ["2006.10.오픈, 472개 매장", "1998.12.뉴욕오픈, 442개 매장", "2018.4.오픈, 40개 매장", "2000.1.오픈, 74개매장", "1983.7.파리오픈, 72개매장"],
                "개요": [    "합리적인 가격에 최신 패션 트렌드를 반영한 캐주얼 의류 브랜드, 주로 젊은 층을 겨냥",
                    "모던하고 세련된 디자인과 고급 소재 프리미엄 컨템포러리 브랜드",
                    "Theory 컨셉을 기반, 일상과 비즈니스에 어울리는 베이직 디자인",
                    "프랑스 고급 여성 패션 브랜드, 파리지앵 스타일",
                    "프랑스 언더웨어 및 홈웨어 브랜드, 여성스러운 디자인과 독특한 프린트 강조"
                ]   }

                # 데이터프레임 생성
            df = pd.DataFrame(data).reset_index(drop = True)
                # 스타일 적용 및 표 출력
            # HTML 스타일 적용
            st.markdown("""
                <style>
                    thead th {
                        color: black !important;
                        text-align: center !important;
                    }
                    tbody td {
                        text-align: center !important;
                    }
                </style>
            """, unsafe_allow_html=True)

            # 표 출력
            st.table(df)


            col1, col2 = st.columns([1, 1])  # 야나이타다시 회장, 최초 태동 소개
            
            with col1:
                st.image("https://i.namu.wiki/i/5XLO954ULu21d-lX8nImMSHx7sccSGOxa8Z_vVyMuBcXLUbtCCBwmerTzCo9gwjOVNSkuKGpTkHOVuTr-cCGdhnJEmRG6eg5veC-eiADEopRUh1OabxDk2xAJs85xYIPD99R29wQ9VAsJDcRMyhX9w.webp", caption="야나이타다시 회장", use_column_width=True)

            with col2:  
                st.subheader("야나이다다시 회장(1949년생)")
                st.write("- 2020년 포브스 선정 세계 부자순위 30위, 일본 부호순위 1위(24년 재산은 5조 9천억엔(약 51조 3천억원)")
                st.write("- 와세다대 정치경제학부 졸업, 1972년 아버지가 운영하던 ‘오고리 상사’(남성 양복점) 입사")
                st.write("- 1984년 히로시마에 첫 UNIQLO 상점 개점")
                st.write("- 미국 대학 구내 매점의 판매방식에서 아이디어 착안(직원의 안내설명 → 고객이 둘러보고 선택)")

                st.write("- '빨리 실패하고, 빨리 경험과 깨달음을 알고, 빨리 수습하고, 빨리 새롭게 도전하라' ")
                st.write("- GAP의 운영방식을 많이 참고한 것으로 알려짐 → SPA 개념 도입")

            # Display images and text in a two-column layout
            col1, col2, col3 = st.columns([1, 1, 1])  # Adjust the width ratio as needed

            with col1:
                # Display the two images on the left side
                st.image(r"C:\Users\USER\Desktop\presentation\오고리상사.png", caption="야나이타다시 부자", use_column_width=True)

            with col2:
                st.image(r"C:\Users\USER\Desktop\presentation\오고리상사1.jpg", caption="오고리상사 상가(야마구치현)", use_column_width=True)
                st.image("https://www.fastretailing.com/eng/about/photolibrary/images/photolib_1stl.jpg", caption="유니클로 1호점(히로시마)", use_column_width=True)

            with col3 :  
                # 지도 생성 - 원하는 위치의 위도와 경도로 설정
                
                latitude = 33.959243535398144
                longitude = 131.2428536045933
                map_obj = folium.Map(location=[latitude, longitude], zoom_start=13)
                l1, l2 = 34.39093082114452, 132.4560791828573
                # 마커 추가
                folium.Marker([latitude, longitude], popup="오고리상사",icon=folium.Icon(color="blue")).add_to(map_obj)
                folium.Marker([l1, l2], popup="유니클로1호점(히로시마)",icon=folium.Icon(color="red")).add_to(map_obj)
                

                # Streamlit에서 folium 지도 표시
                st_folium(map_obj, width=700)


        elif selected_sub_menu == "연혁":  #border-left: 4px solid red;
            # 타임라인 스타일 정의
            st.markdown("""
                <style>
                    .timeline {
                        font-family: Arial, sans-serif;
                        padding: 10px;
                        
                    }
                    .timeline-item {
                        margin-left: 20px;
                        padding: 10px;
                        border-top: 1px dashed #ccc;
                        display: flex;
                        align-items: center;
                    }
                    .timeline-item p {
                        margin: 0;
                    }
                    .timeline-date {
                        font-weight: bold;
                        color: #333;
                        min-width: 70px;
                    }
                    .timeline-text {
                        flex-grow: 1;
                        color: #333;
                    }
                    .timeline-image {
                        margin-left: 15px;
                        width: 100px;
                        height: auto;
                    }
                </style>
            """, unsafe_allow_html=True)

            # 타임라인 내용
            timeline_content = [
                {
                    "date": "1984년",
                    "text": "히로시마에 첫 UNIQLO 상점 개점",
                    "image": "https://www.fastretailing.com/eng/about/history/images/1984-06.jpg",
                    "link": "https://www.fastretailing.com/eng/about/history/2003.html"
                },
                {
                    "date": "1994년",
                    "text": "히로시마거래소 주식상장",
                    "image": None,
                    "link": None
                },
                {
                    "date": "2005년 9월",
                    "text": "서울, 미국뉴저지, 홍콩 침사추이, 도쿄긴자 오픈",
                    "image": "https://www.fastretailing.com/eng/about/history/images/200509_korea.jpg",
                    "link": None
                },
                {
                    "date": "2006~2007년",
                    "text": "일본 도레이산업(화학섬유업체)제휴, 히트텍 대박",
                    "image": "https://i.namu.wiki/i/DPq6E2VYRGiCqPObFLATWiWJZ5csWlv1eHCyXpCpLbsYzUmP1tOCtpp2WTZ-4xZzmXvlu9DFCBibkl9c_rY33A.png",
                    "link": "https://m.news.zum.com/articles/4945754"
                },
                {
                    "date": "2017년",
                    "text": "아리아케프로젝트",
                    "image": "https://www.fpost.co.kr/board/data/editor/1911/658066bb906def7c4643cb6242f7b16f_1574129381_7826.jpg",
                    "link": "https://fpost.co.kr/board/bbs/board.php?wr_id=753&bo_table=newsinnews"
                },
                {
                    "date": "2024년",
                    "text": "연매출 3조엔 돌파",
                    "image": "https://www.apparelnews.co.kr/upfiles/manage/202410/0d5210df2443c0ebafd071ca461e4c71.jpg",
                    "link": "https://www.apparelnews.co.kr/news/news_view/?cat=CAT160&idx=213645"
                }
            ]

            # 타임라인 표시
            st.markdown("<div class='timeline'>", unsafe_allow_html=True)
            for item in timeline_content:
                st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)
                st.markdown(f"<span class='timeline-date'>{item['date']}</span>", unsafe_allow_html=True)
                st.markdown(f"<span class='timeline-text'>{item['text']}</span>", unsafe_allow_html=True)
                
                # 이미지가 있는 경우 링크 포함
                if item["image"]:
                    image_html = f"""
                        <a href="{item['link']}" target="_blank">
                            <img src="{item['image']}" class="timeline-image">
                        </a>
                    """
                    st.markdown(image_html, unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)



        elif selected_sub_menu == "재무":
            # 데이터 생성
            data = {
                "Company Name (Flagship Brand)": [
                    "Inditex, S.A. (ZARA)", "H & M Hennes & Mauritz AB", "FAST RETAILING CO., LTD. (UNIQLO)", 
                    "Gap Inc.", "lululemon athletica inc.", "PVH Corp. (Calvin Klein, Tommy Hilfiger)", 
                    "Next plc", "Ralph Lauren Corporation", "Victoria's Secret & Co.", 
                    "American Eagle Outfitters Inc."
                ],
                "Country and Region": [
                    "Spain", "Sweden", "Japan", 
                    "USA", "USA", "USA", 
                    "UK", "USA", "USA", 
                    "USA"
                ],
                "End of Fiscal Year": [
                    "Jan. 2024", "Nov. 2023", "Aug. 2023", 
                    "Feb. 2024", "Jan. 2024", "Feb. 2024", 
                    "Jan. 2024", "Apr. 2023", "Feb. 2024", 
                    "Feb. 2024"
                ],
                "Sales (Trillion of yen)": [
                    5.87, 3.44, 2.76, 
                    2.24, 1.44, 1.38, 
                    1.04, 0.97, 0.93, 
                    0.79
                ],
                "Sales (Billions of dollar)": [
                    38.9, 22.8, 18.3, 
                    14.8, 9.6, 9.2, 
                    6.9, 6.4, 6.1, 
                    5.2
                ],
                "Change (%) (local base)": [
                    "+10.4", "+5.6", "+20.2", 
                    "-4.7", "+18.6", "+2.2", 
                    "+9.1", "+3.6", "-2.6", 
                    "+5.4"
                ]
            }

            # 데이터프레임 생성
            df = pd.DataFrame(data, dtype = str)

            # Streamlit 앱 제목
            st.title("Industry Ranking : 3위")
            st.caption("Major Global Apparel Manufacturer and Retailer")

            # 데이터프레임 스타일 설정
            styled_df = df.style.applymap(
                lambda x: 'background-color: red; color: white' if x == "FAST RETAILING CO., LTD. (UNIQLO)" else ""
            ).set_properties(
                **{'text-align': 'center'}
            ).set_table_styles([
                {'selector': 'th', 'props': [('background-color', '#333'), ('color', 'white'), ('text-align', 'center')]}
            ])

            # 스타일 적용한 데이터프레임 표시
            st.write(styled_df.to_html(), unsafe_allow_html=True)


            # 데이터 준비 - 차트
            data = {
                "Fiscal Year": ["F92", "F93", "F94", "F95", "F96", "F97", "F98", "F99", "F00", 
                                "F01", "F02", "F03", "F04", "F05", "F06", "F07", "F08", "F09", 
                                "F10", "F11", "F12", "F13", "F14", "F15", "F16", "F17", 
                                "F18", "F19", "F20", "F21", "F22", "F23", "F24"],
                "Net Sales (Billions of Yen)": [14.339, 25.037, 33.336, 48.692, 59.959, 75.020, 83.120, 111.081, 228.985, 
                                                418.561, 344.170, 309.789, 339.999, 383.973, 448.819, 525.203, 586.451, 
                                                685.043, 814.811, 820.349, 928.669, 1143.003, 1382.907, 1681.7, 1786.4, 
                                                1861.9, 2130.0, 2290.5, 2008.8, 2132.9, 2301.1, 2766.5, 3103.8],
                "Operating Income (Billions of Yen)": [0.935, 2.163, 3.266, 4.164, 4.441, 5.263, 6.011, 14.343, 60.627, 
                                                        102.081, 50.418, 41.308, 63.954, 56.692, 70.355, 64.963, 87.493, 
                                                        108.639, 132.378, 116.365, 126.451, 132.920, 148.646, 164.4, 
                                                        127.2, 176.4, 236.2, 257.6, 149.3, 249.0, 297.3, 381.0, 500.9],
                "Stores (including franchise stores)": [62, 90, 2982, 176, 229, 276, 336, 368, 433, 519, 585, 622, 655, 1232, 
                                                        1632, 1828, 1958, 2258, 2203, 2088, 2222, 2449, 2753, 2978, 
                                                        3160, 3294, 3445, 3589, 3630, 3527, 3562, 3578, 3595]
            }


            # 환율 설정 및 달러로 변환
            yen_to_dollar = 0.007
            df = pd.DataFrame(data)
            df["Net Sales (Billions of Dollar)"] = df["Net Sales (Billions of Yen)"] * yen_to_dollar
            df["Operating Income (Billions of Dollar)"] = df["Operating Income (Billions of Yen)"] * yen_to_dollar

            # 연도를 끝 2자리로 변환
            # df["Fiscal Year"] = df["Fiscal Year"].apply(lambda x: str(x[-2:]) if x.startswith("FY") else x)

            # Streamlit 앱 제목
            st.title("UNIQLO Financial Data")

            # 차트 1 - Net Sales와 Store Count
            fig1 = go.Figure()

            # Net Sales는 막대그래프
            fig1.add_trace(go.Bar(
                x=df["Fiscal Year"],
                y=df["Net Sales (Billions of Dollar)"],
                name="Net Sales (Billions of Dollar)",
                marker_color="skyblue"
            ))

            # Store Count는 꺾은선 그래프, 오른쪽 축
            fig1.add_trace(go.Scatter(
                x=df["Fiscal Year"],
                y=df["Stores (including franchise stores)"],
                name="Store Count",
                mode="lines+markers",
                marker_color="green",
                yaxis="y2"
            ))

            # 레이아웃 설정
            fig1.update_layout(
                title="Net Sales and Store Count Over Time",
                xaxis_title="Fiscal Year",
                yaxis_title="Net Sales (Billions of Dollar)",
                yaxis2=dict(
                    title="Store Count",
                    overlaying="y",
                    side="right"
                ),
                legend=dict(x=0.01, y=0.99)
            )

            # 차트 출력
            st.plotly_chart(fig1)

            # 차트 2 - Operating Income와 Store Count
            fig2 = go.Figure()

            # Operating Income는 막대그래프
            fig2.add_trace(go.Bar(
                x=df["Fiscal Year"],
                y=df["Operating Income (Billions of Dollar)"],
                name="Operating Income (Billions of Dollar)",
                marker_color="salmon"
            ))

            # Store Count는 꺾은선 그래프, 오른쪽 축
            fig2.add_trace(go.Scatter(
                x=df["Fiscal Year"],
                y=df["Stores (including franchise stores)"],
                name="Store Count",
                mode="lines+markers",
                marker_color="green",
                yaxis="y2"
            ))

            # 레이아웃 설정
            fig2.update_layout(
                title="Operating Income and Store Count Over Time",
                xaxis_title="Fiscal Year",
                yaxis_title="Operating Income (Billions of Dollar)",
                yaxis2=dict(
                    title="Store Count",
                    overlaying="y",
                    side="right"
                ),
                legend=dict(x=0.01, y=0.99)
            )

            # 차트 출력
            st.plotly_chart(fig2)


            # 데이터 준비
            data = {
                "Year": [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                "UNIQLO Japan Sales": [683.3, 715.6, 780.1, 799.8, 810.7, 864.7, 872.9, 806.8, 842.6, 810.2, 890.4, 932.2],
                "UNIQLO Japan Operating Income": [95.2, 106.3, 117.2, 102.4, 95.9, 119.0, 102.4, 104.6, 123.2, 124.0, 117.8, 155.8],
                "UNIQLO Japan Stores": [853, 852, 841, 837, 831, 827, 817, 813, 810, 809, 800, 797],
                "UNIQLO International Sales": [251.1, 413.6, 603.6, 655.4, 708.1, 896.3, 1026.0, 843.9, 930.1, 1118.7, 1437.1, 1711.8],
                "UNIQLO International Operating Income": [12.4, 32.9, 43.3, 37.4, 73.1, 118.8, 138.9, 50.2, 111.2, 158.3, 226.9, 283.4],
                "UNIQLO International Stores": [446, 633, 798, 958, 1089, 1241, 1379, 1439, 1502, 1585, 1634, 1698],
                "GU Sales": [None, None, None, None, 199.1, 211.8, 238.7, 246.0, 249.4, 246.0, 295.2, 319.1],
                "GU Operating Income": [None, None, None, None, 135.0, 11.7, 28.1, 21.8, 20.1, 16.6, 26.1, 33.7],
                "GU Stores": [None, None, None, None, 372, 393, 421, 436, 439, 449, 463, 472],
                "Global Brands Sales": [206.2, 251.2, 295.3, 328.5, 141.0, 154.4, 149.9, 109.6, 108.2, 123.1, 141.6, 138.8],
                "Global Brands Operating Income": [16.7, -4.1, 14.4, 9.5, 0.5, -4.1, 3.6, -12.7, -16.3, -0.7, -3.0, 0.6],
                "Global Brands Stores": [1150, 1268, 1339, 1365, 1002, 984, 972, 942, 776, 719, 681, 628]
            }

            # 환율 설정 및 달러로 변환
            yen_to_dollar = 0.007
            df = pd.DataFrame(data)
            for col in df.columns:
                if "Sales" in col or "Operating Income" in col:
                    df[col] = df[col].apply(lambda x: x * yen_to_dollar if pd.notnull(x) else x)

            # Streamlit 앱 제목
            st.title("Group Brands Financial Data")

            # 차트 1 - 매출과 직영매장수 (UNIQLO Japan, UNIQLO International, GU, Global Brands)
            fig1 = go.Figure()

            # 매출 데이터 추가 (막대그래프)
            for brand in ["UNIQLO Japan", "UNIQLO International", "GU", "Global Brands"]:
                fig1.add_trace(go.Bar(
                    x=df["Year"],
                    y=df[f"{brand} Sales"],
                    name=f"{brand} Sales (Billions of Dollar)",
                ))

            # 직영매장수 데이터 추가 (꺾은선 그래프)
            for brand in ["UNIQLO Japan", "UNIQLO International", "GU", "Global Brands"]:
                fig1.add_trace(go.Scatter(
                    x=df["Year"],
                    y=df[f"{brand} Stores"],
                    name=f"{brand} Stores",
                    mode="lines+markers",
                    yaxis="y2"
                ))

            # 레이아웃 설정
            fig1.update_layout(
                title="Sales and Store Count Over Time",
                xaxis_title="Year",
                yaxis_title="Sales (Billions of Dollar)",
                yaxis2=dict(
                    title="Store Count",
                    overlaying="y",
                    side="right"
                ),
                barmode='group'
            )

            # 차트 출력
            st.plotly_chart(fig1)

            # 차트 2 - 영업이익과 직영매장수 (UNIQLO Japan, UNIQLO International, GU, Global Brands)
            fig2 = go.Figure()

            # 영업이익 데이터 추가 (막대그래프)
            for brand in ["UNIQLO Japan", "UNIQLO International", "GU", "Global Brands"]:
                fig2.add_trace(go.Bar(
                    x=df["Year"],
                    y=df[f"{brand} Operating Income"],
                    name=f"{brand} Operating Income (Billions of Dollar)",
                ))

            # 직영매장수 데이터 추가 (꺾은선 그래프)
            for brand in ["UNIQLO Japan", "UNIQLO International", "GU", "Global Brands"]:
                fig2.add_trace(go.Scatter(
                    x=df["Year"],
                    y=df[f"{brand} Stores"],
                    name=f"{brand} Stores",
                    mode="lines+markers",
                    yaxis="y2"
                ))

            # 레이아웃 설정
            fig2.update_layout(
                title="Operating Income and Store Count Over Time",
                xaxis_title="Year",
                yaxis_title="Operating Income (Billions of Dollar)",
                yaxis2=dict(
                    title="Store Count",
                    overlaying="y",
                    side="right"
                ),
                barmode='group'
            )

            # 차트 출력
            st.plotly_chart(fig2)




        elif selected_sub_menu == "비즈니스 분석":
            st.title("Uniqlo SWOT Analysis")

            # 4분면 레이아웃 설정
            col1, col2 = st.columns(2)

            # Strengths 섹션
            with col1:
                st.subheader("Strengths")
                st.markdown("""
                - **기술 혁신**: HeatTech, AIRism 등 기술로 브랜드 차별화 성공
                - **효율적인 공급망**: SPA 모델을 통한 비용 절감
                - **브랜드 포지셔닝**: 고품질과 심플함으로 다양한 고객층 확보
                """)

            # Weaknesses 섹션
            with col2:
                st.subheader("Weaknesses")
                st.markdown("""
                - **중국 의존도**: 매출 상당 부분이 중국에 의존
                - **온라인 성과 부족**: 온라인 판매 비중이 낮아 성장 기회 존재
                - **지속 가능성 문제**: 환경 문제 해결을 위한 지속 가능성 강화 필요
                """)

            # Opportunities 섹션
            with col1:
                st.subheader("Opportunities")
                st.markdown("""
                - **글로벌 확장**: 북미, 유럽 시장 및 스포츠/홈웨어 카테고리 확장 가능
                - **디지털 혁신**: 온라인 채널 및 옴니채널 통합으로 디지털 판매 성장 촉진
                """)

            # Threats 섹션
            with col2:
                st.subheader("Threats")
                st.markdown("""
                - **경쟁 심화**: H&M, ZARA 등과의 치열한 경쟁
                - **경제적 불확실성**: 경기 불황, 공급망 문제 등으로 비용 상승 우려
                """)

            st.image(r"C:\Users\USER\Desktop\presentation\uniqlo_대륙별.png")
            st.markdown(
                """
                - ([유니클로, 자라 제치고 세계 최대 의류회사 됐다](https://www.hankyung.com/article/202102179714i))
                """
            )
            # 분석 요약
            st.markdown("""
            ---
            Uniqlo는 기술 혁신과 글로벌 확장을 통해 강점을 강화하고 있지만, 경쟁업체에 대비하고, 온라인 판매 활성화 필요
            """)

            st.title("Uniqlo - Porter's 5 Forces Analysis")

            # Define the 5 Forces data in a structured format
            forces_data = {
                "경쟁자 간 경쟁": [
                    "Zara, H&M 등과의 치열한 경쟁",
                    "고객의 브랜드 전환 비용이 낮아 지속적인 차별화 필요"
                ],
                "신규 진입자의 위협": [
                    "패스트 패션 시장 진입 장벽 낮음",
                    "브랜드 인지도와 규모로 일부 보호"
                ],
                "대체재의 위협": [
                    "다양한 브랜드로 인해 대체재 위협 큼",
                    "고품질 기본 의류 제공으로 영향 최소화"
                ],
                "고객의 협상력": [
                    "다양한 선택지로 인해 협상력 중간에서 높음",
                    "합리적 가격과 품질로 고객 충성도 유지"
                ],
                "공급자의 협상력": [
                    "대규모 구매 및 자체 소재 개발로 공급자 의존도 낮춤",
                    "공급자의 협상력 낮은 편"
                ]
            }

            # Streamlit layout styling
            st.markdown("""
                <style>
                .quadrant {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 20px;
                    justify-content: center;
                    text-align: center;
                }
                .quadrant-item {
                    background-color: #f8f8f8;
                    padding: 5px;
                    border-radius: 5px;
                    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                    width: 90%;
                    margin-bottom: 15px;
                }
                .quadrant-title {
                    font-size: 1.5em;
                    font-weight: bold;
                    color: #333;
                    margin-bottom: 10px;
                }
                .quadrant-content {
                    color: #555;
                }
                </style>
            """, unsafe_allow_html=True)

            # Display the 5 Forces analysis in shaded boxes
            for force, points in forces_data.items():
                st.markdown(f"<div class='quadrant-title'>{force}</div>", unsafe_allow_html=True)
                st.markdown("<div class='quadrant-item'>", unsafe_allow_html=True)

                st.markdown("<div class='quadrant-content'><ul>", unsafe_allow_html=True)

                for point in points:
                    st.markdown(f"<li>{point}</li>", unsafe_allow_html=True)
                st.markdown("</ul></div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

            # Streamlit 페이지 기본 설정
            # st.set_page_config(page_title="Fast Retailing & Nikkei 225 Index Comparison", layout="wide")

            # 타이틀 및 설명
            st.title("Fast Retailing vs Nikkei 225 Index")
            st.write("2000년부터 현재까지의 Fast Retailing 주가와 Nikkei 225 지수를 비교하는 차트입니다.")

            # 데이터 로드
            @st.cache_data(ttl=86400)  # 1 day cache
            def load_data():
                # Fast Retailing (Ticker: 9983.T) & Nikkei 225 (^N225) 데이터 가져오기
                end_date = datetime.date.today()
                fast_retailing = yf.download("9983.T", start="2000-01-01", end=end_date, progress=False)['Close'].squeeze()
                nikkei = yf.download("^N225", start="2000-01-01", end=end_date, progress=False)['Close'].squeeze()

                # 데이터 존재 여부 확인
                if fast_retailing.empty or nikkei.empty:
                    st.error("데이터 로드에 실패했습니다.")
                    return None

                # 필요 컬럼 선택 (종가만 사용) 및 인덱스를 데이터프레임으로 생성
                data = pd.DataFrame({
                    'Fast Retailing': fast_retailing,
                    'Nikkei 225': nikkei
                })

                return data

            # 데이터 로드
            data = load_data()

            # 데이터가 성공적으로 로드되었는지 확인
            if data is not None:
                # 데이터 시각화
                st.subheader("Fast Retailing과 Nikkei 225 지수 비교")
                st.line_chart(data)

                # 로그 스케일 옵션
                use_log = st.checkbox("로그 스케일로 보기")

                # 차트 그리기
                fig, ax = plt.subplots(figsize=(14, 7))
                if use_log:
                    ax.set_yscale('log')
                    
                data.plot(ax=ax)
                ax.set_title("Fast Retailing vs Nikkei 225 Index (2000 - Present)")
                ax.set_ylabel("Index Level")
                ax.set_xlabel("Date")
                st.pyplot(fig)
            else:
                st.write("데이터 로드에 실패했습니다. 다시 시도해 주세요.")


        elif selected_sub_menu == "AI전략":
            # 페이지 제목
            st.title("Uniqlo의 디지털 전환 전략")
            col1, col2 = st.columns(2)
            with col1:
                st.image("http://www.fpost.co.kr/board/data/editor/1911/658066bb906def7c4643cb6242f7b16f_1574129381_7826.jpg", caption="패스트리테일링 아리아케 본부", use_column_width=True)
            with col2:
                st.image(r"C:\Users\USER\Desktop\presentation\아리아케1.png", caption="기존 본사와 현재 아리아케 위치", use_column_width=True)

            # 아리아케 프로젝트 개요
            st.subheader("아리아케 프로젝트")
            st.markdown("""
            - **2017년 도쿄 롯폰기에서 아리아케로 이전**
            - **목적**: 제품 기획, 생산, 진열까지 걸리는 시간을 줄여 불량재고 감소
            - **구성**: 1~5층은 물류, 6층은 사무실로 구성. 기획, 디자인, IT 인력 1,000명 집결
            - **실시간 공유**: 소비자 수요와 생산 정보를 실시간으로 공유
            """)

            # 세부 전략
            st.subheader("디지털 전환 세부 전략")
            st.image(r"C:\Users\USER\Desktop\presentation\아리아케.png", caption="아리아케 프로젝트 소개", use_column_width=True)
            # 고객 중심 플랫폼 구축
            st.markdown("### 1. 고객 중심 플랫폼 구축")
            st.markdown("""
            - **고객 의견 수집**: 1억 4천만 앱 회원 보유, 매일 2,700만 개 의견 수집 및 분석
            - **고객 맞춤 제품 개발**: 고객이 원하는 제품과 서비스를 개발하여 제공
            """)

            # 정보를 제품으로 전환
            st.markdown("### 2. 정보를 제품으로 전환")
            st.markdown("""
            - **제품 개발**: 고객 의견을 바탕으로 2020년에 50개 이상의 제품 개발
            - **사진 스튜디오 설립**: 아리아케 본사에 스튜디오를 설립하여 제품 가치를 명확히 전달
            """)

            # 공급망 혁신
            st.markdown("### 3. 공급망 혁신")
            st.markdown("""
            - **파트너십**: 로봇제조사 MUJIN, 무인상품관리회사 Exotec Solutions와 협력해 창고 자동화 추진
            - **AI 기반 수요 예측**: AI를 활용한 수요 예측으로 생산 및 재고 계획의 정확성 증대
            - **맞춤형 주문 서비스**: 고객이 신체 치수와 디자인을 선택하면 10일 내 제품 배송
            - **물류 체계 자동화**: RFID 태그로 재고 및 판매 동향 파악, 주문에서 출하까지 시간을 15분~1시간 이내로 단축
            """)

            # 온라인과 오프라인 매장의 통합
            st.markdown("### 4. 온라인과 오프라인 매장의 통합")
            st.markdown("""
            - **전자 상거래 활성화**: 구글, 엑센추어와 파트너십으로 빅데이터 활용
            - **실시간 정보 공유**: 매장 인기 상품과 구매 수량 정보가 실시간으로 전달되어 전 사원이 공유
            - **주 단위 생산 체계**: 최신 유행과 고객 취향을 실시간 반영하여 신상품을 주 단위로 기획·생산·진열
            """)

            # 협업 기반의 근무 방식 도입
            st.markdown("### 5. 협업 기반의 근무 방식 도입")
            st.markdown("""
            - **상품별 팀제 도입**: 하의, 상의, 외투, 내의 등 상품군별로 기획부터 판매까지 통합 관리
            - **편의점 픽업 서비스**: 온라인 주문 상품을 세븐일레븐, 패밀리마트 등 4만 3천여 편의점에서 픽업 가능
            """)

        elif selected_sub_menu == "결론" : 
            st.subheader("유니클로의 특징")

            st.markdown('<div class="current-status">', unsafe_allow_html=True)

            # 1. 매출 성장
            st.subheader("1. 매출 성장")
            st.markdown("""
                - 일본 제품 불매 운동, 중국과의 갈등, 경제침체 우려 등에도 불구하고 꾸준한 성장을 유지
                - 아리아케프로젝트 등 물류최적화, 효율성 강화, 디지털 전환, 꾸준한 품질을 바탕으로 24년 매출 3조엔 돌파

            """)

            # 2. 제품 전략
            st.subheader("2. 제품 전략")
            st.markdown("""
                - 기본적이고 기능성을 강조한 제품으로 모든 연령층을 타겟팅.
                - 기술력을 접목한 기능성 의류인 히트텍(HEATTECH), 에어리즘(AIRism) 등을 선보임.
                - 다양한 콜라보레이션을 통해 제품 차별화를 시도하고 있으며, 장기간 판매되는 기본 제품 라인을 유지.
            """)

            # 3. 디지털 전환
            st.subheader("3. 디지털 전환")
            st.markdown("""
                - 온라인과 오프라인 경계를 허무는 옴니채널 전략 강화.
                - 본사에 촬영 스튜디오와 글로벌 고객센터를 마련하여 디지털 콘텐츠와 고객 소통을 강화.
                - AI 기반 패션 코디 서비스 'UNIQLO IQ' 도입으로 고객에게 맞춤형 추천 제공.
            """)

            st.markdown('</div>', unsafe_allow_html=True)


    elif selected_brand == "ZARA":
        if selected_sub_menu == "기업개요":

            # 좌우 레이아웃 구성
            col1, col2 = st.columns([1, 2])

            # 왼쪽에 로고 표시
            with col1:
                st.image("https://www.industriall-union.org/sites/default/files/styles/article_top_image_w1440/public/uploads/images/2020/ROMANIA/screen_shot_2020-10-28_at_13.38.44.png?itok=Pjh_UMF1", caption="Inditex, 주요 브랜드", use_column_width=True)


            # 오른쪽에 기업 정보 요약
            with col2:
                st.subheader("ZARA의 모기업 인디텍스 개요")
                st.markdown("""
                - **본사 위치**: 스페인 갈리시아 지방 라코루냐 주 아르테익소
                - **상장**: 마드리드 증권거래소 상장, 스페인 상장사 중 시가총액 1위
                - **주요 브랜드**: 7개 주요 브랜드 보유 (한국 운영 브랜드: ZARA, Massimo Dutti, ZARA Home)
                - **글로벌 규모**: 2024년 3월 기준, 213개국에 5,692개 매장 운영, 총 임직원 16만 명
                """)
                
                st.subheader("2023년 재무 성과")
                st.markdown("""
                - **매출**: 359억 유로 (전년 대비 10.4% 증가)
                - **순이익**: 54억 유로 (전년 대비 30.3% 증가)
                """)
            # INDITEX 주요 브랜드 소개 데이터
            data = {
                "브랜드": ["ZARA", "Pull&Bear", "Massimo Dutti", "Bershka", "Stradivarius", "Oysho", "Uterqüe"],
                "소개": [
                    "- INDITEX의 대표적인 패스트 패션 브랜드\n- 최신 패션 트렌드를 빠르게 반영, 합리적인 가격 제공\n- 의류, 액세서리, 신발, 향수 등 다양한 제품 판매",
                    "- 캐주얼하고 스트리트 감성의 브랜드\n- 20대 젊은층 대상, 편안하고 활동적인 스타일\n- 스트리트 패션에서 영감 받은 디자인",
                    "- 프리미엄 브랜드, 고급스러운 감성 추구\n- 포멀하고 클래식한 스타일로 중·고소득층 인기\n- 품질 높은 소재와 심플한 디자인 제공",
                    "- 10대 후반~20대 초반 타깃의 패션 브랜드\n- 최신 트렌드와 독특한 디자인 제공\n- 합리적인 가격과 파격적인 스타일",
                    "- 여성 타겟 브랜드, 여성스러운 스타일 강조\n- 다양한 패션 욕구를 위한 의류, 액세서리, 신발 제공",
                    "- 언더웨어, 홈웨어, 피트니스웨어, 수영복 전문\n- 편안하면서 세련된 스타일로 여성 소비자 인기",
                    "- 액세서리와 고급 의류 브랜드\n- 고급스럽고 우아한 스타일, ZARA 컬렉션에 통합"
                ]
            }

            # 데이터프레임 생성
            df = pd.DataFrame(data)

            # Streamlit에 표 형태로 출력
            st.title("INDITEX 주요 브랜드 소개")
            st.table(df)

            col1, col2 = st.columns([1, 1])  # 아만시오 오르테가 회장, 설립 배경 소개

            with col1:
                st.image(
                    "http://kosmba.or.kr/data/editor/1805/thumb-ff881acece925a5e028633a41414ce1b_1527089599_0108_600x444.jpg", 
                    caption="아만시오 오르테가 회장", 
                    use_column_width=True
                )

            with col2:
                st.subheader("아만시오 오르테가 회장")
                st.write("- 1936년 스페인 작은 마을에서 출생(철도원 아들)")
                st.write("- 젊은 시절 봉제 공장에서 일하며 패션 업계에 입문")
                st.write("- 1975년, 첫 자라(ZARA) 매장을 스페인 라코루냐에서 개점")
                st.write("- 고객 중심 철학에 기반해 패션 트렌드를 빠르게 반영하는 '패스트 패션' 모델 구축")
                st.write("- 소비자의 니즈에 빠르게 대응하며 합리적인 가격의 고품질 패션을 제공하고자 함")

                st.write("- '옷가게는 생선가게와 같다' 고객이 원할때 제때에 공급해야... FastFashion")
                st.write("- 성공 요인: 신속한 공급망 관리와 트렌드 적응력으로 전 세계적 성장을 이루어냄")

        elif selected_sub_menu == "연혁":
            # 스타일 설정
            st.markdown("""
                <style>
                    .timeline {
                        font-family: Arial, sans-serif;
                        padding: 10px;
                    }
                    .timeline-item {
                        margin-left: 20px;
                        padding: 10px;
                        border-top: 1px dashed #ccc;
                        display: flex;
                        align-items: center;
                    }
                    .timeline-date {
                        font-weight: bold;
                        color: #333;
                        min-width: 70px;
                    }
                    .timeline-text {
                        flex-grow: 1;
                        color: #333;
                    }
                    .timeline-image {
                        margin-left: 15px;
                        width: 100px;
                        height: auto;
                    }
                </style>
            """, unsafe_allow_html=True)

            # 타임라인 내용
            timeline_content = [
                {
                    "date": "1963년",
                    "text": "아만시오 오르테가가 의류 제조 공장을 설립하며 사업 시작",
                    "image": None,
                    "link": None
                },
                {
                    "date": "1975년",
                    "text": "오르테가가 39세에 첫 '자라(Zara)' 매장을 오픈, 제조업자가 직접 소매까지 하는 사업 모델 시작",
                    "image": "https://cdn.sisunnews.co.kr/news/photo/201609/41587_63032_629.jpg",
                    "link": None
                },
                {
                    "date": "1984년",
                    "text": "IT 전문가 조세 마리아 카스텔라노 영입, 컴퓨터를 이용해 납기를 6개월에서 2주로 단축하는 SPA 모델 개발",
                    "image": None,
                    "link": None
                },
                {
                    "date": "1985년",
                    "text": "인디텍스(Inditex) 그룹으로 회사 통합, 스페인 내 자라 매장 80개로 확장, 해외 진출 시작",
                    "image": None,
                    "link": None
                },
                {
                    "date": "1991년",
                    "text": "신규 브랜드 발굴 시작, 풀앤베어(Pull&Bear) 런칭",
                    "image": None,
                    "link": None
                },
                {
                    "date": "1995년",
                    "text": "마시모두띠(Massimo Dutti) 인수",
                    "image": None,
                    "link": None
                },
                {
                    "date": "1998년",
                    "text": "버쉬카(Bershka) 런칭",
                    "image": None,
                    "link": None
                },
                {
                    "date": "1999년",
                    "text": "스트라디바리우스(Stradivarius) 인수",
                    "image": None,
                    "link": None
                },
                {
                    "date": "2001년",
                    "text": "기업 공개(IPO) 실시, 지분 26% 매각",
                    "image": None,
                    "link": None
                },
                {
                    "date": "2003년",
                    "text": "자라홈(Zara Home) 런칭",
                    "image": None,
                    "link": None
                },
                {
                    "date": "2008년",
                    "text": "유텐(Uterqüe) 런칭",
                    "image": None,
                    "link": None
                },
                {
                    "date": "2011년",
                    "text": "외부 경영 전문가 파블로 이슬라(Pablo Isla)를 CEO로 영입",
                    "image": None,
                    "link": None
                },
                {
                    "date": "2023년",
                    "text": "매출 359억 유로, 순이익 54억 유로 달성. 약 90개국에 5,700여 개 매장 운영, 16만 명 이상의 직원 보유",
                    "image": None,
                    "link": None
                }
            ]

            # 타임라인 표시
            st.markdown("<div class='timeline'>", unsafe_allow_html=True)
            for item in timeline_content:
                st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)
                st.markdown(f"<span class='timeline-date'>{item['date']}</span>", unsafe_allow_html=True)
                st.markdown(f"<span class='timeline-text'>{item['text']}</span>", unsafe_allow_html=True)
                
                # 이미지가 있는 경우 링크 포함
                if item["image"]:
                    image_html = f"""
                        <a href="{item['link']}" target="_blank">
                            <img src="{item['image']}" class="timeline-image">
                        </a>
                    """
                    st.markdown(image_html, unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        elif selected_sub_menu == "재무":
                        # 데이터 준비
            data_sales = {
                "year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
                "sales": [12.53, 13.79, 15.95, 16.72, 18.12, 20.90, 23.31, 25.34, 26.15, 28.29, 20.40, 27.72, 32.57, 35.95],
                "stores": [5044, 5527, 6009, 6340, 6683, 7013, 7292, 7475, 7490, 7469, 6829, 6477, 5815, 5692]
            }

            data_income = {
                "year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
                "net_income": [1.741, 1.946, 2.367, 2.382, 2.51, 2.882, 3.157, 3.368, 3.444, 3.647, 1.104, 3.25, 4.147, 5.395],
                "stores": [5044, 5527, 6009, 6340, 6683, 7013, 7292, 7475, 7490, 7469, 6829, 6477, 5815, 5692]
            }

            # 환율 설정 (1 유로 = 1.1 달러)
            euro_to_dollar = 1.1
            df_sales = pd.DataFrame(data_sales)
            df_income = pd.DataFrame(data_income)

            # 유로에서 달러로 변환
            df_sales["sales"] = df_sales["sales"] * euro_to_dollar
            df_income["net_income"] = df_income["net_income"] * euro_to_dollar

            # Streamlit 앱 제목
            st.title("INDITEX Financial Data")

            # 차트 1 - Sales와 Store Count
            fig1 = go.Figure()

            # Sales는 막대그래프
            fig1.add_trace(go.Bar(
                x=df_sales["year"],
                y=df_sales["sales"],
                name="Sales (Billions of Dollar)",
                marker_color="skyblue"
            ))

            # Store Count는 꺾은선 그래프, 오른쪽 축
            fig1.add_trace(go.Scatter(
                x=df_sales["year"],
                y=df_sales["stores"],
                name="Store Count",
                mode="lines+markers",
                marker_color="green",
                yaxis="y2"
            ))

            # 레이아웃 설정
            fig1.update_layout(
                title="Sales and Store Count Over Time",
                xaxis_title="Year",
                yaxis_title="Sales (Billions of Dollar)",
                yaxis2=dict(
                    title="Store Count",
                    overlaying="y",
                    side="right"
                ),
                legend=dict(x=0.01, y=0.99)
            )

            # 차트 출력
            st.plotly_chart(fig1)

            # 차트 2 - Net Income와 Store Count
            fig2 = go.Figure()

            # Net Income는 막대그래프
            fig2.add_trace(go.Bar(
                x=df_income["year"],
                y=df_income["net_income"],
                name="Net Income (Billions of Dollar)",
                marker_color="salmon"
            ))

            # Store Count는 꺾은선 그래프, 오른쪽 축
            fig2.add_trace(go.Scatter(
                x=df_income["year"],
                y=df_income["stores"],
                name="Store Count",
                mode="lines+markers",
                marker_color="green",
                yaxis="y2"
            ))

            # 레이아웃 설정
            fig2.update_layout(
                title="Net Income and Store Count Over Time",
                xaxis_title="Year",
                yaxis_title="Net Income (Billions of Dollar)",
                yaxis2=dict(
                    title="Store Count",
                    overlaying="y",
                    side="right"
                ),
                legend=dict(x=0.01, y=0.99)
            )

            # 차트 출력
            st.plotly_chart(fig2)


            # 매장수가 급감한 것이 팩트인가?
            st.markdown("[ZARA 전 세계 매장 중 300개 폐쇄한다](https://www.mediaville.co.kr/news/articleView.html?idxno=133)")
            st.markdown("[인디텍스, 자라 등 1200개 매장 문 닫고 온라인 집중](https://news.zum.com/articles/60697461)")


        elif selected_sub_menu == "비즈니스 분석":
            # 앱 제목
            st.title("Inditex SWOT Analysis")

            # 4분면 레이아웃 설정
            col1, col2 = st.columns(2)

            # Strengths 섹션
            with col1:
                st.subheader("Strengths")
                st.markdown("""
                - **강력한 브랜드 포트폴리오**: Zara, Pull&Bear, Massimo Dutti 등 인기 브랜드 보유
                - **수직 통합된 비즈니스 모델**: 디자인부터 유통까지 전 과정 통제
                - **글로벌 입지**: 88개국에 6,460개 이상 매장 운영
                - **빠른 트렌드 대응**: 3주 내 새 디자인 출시 가능
                - **혁신과 기술 투자**: AI와 데이터 분석 활용으로 고객 선호 파악 및 재고 최적화
                """)

            # Weaknesses 섹션
            with col2:
                st.subheader("Weaknesses")
                st.markdown("""
                - **노동 및 공급망 이슈**: 과거 윤리적 문제로 비판받은 기록
                - **제한적인 제품 범위**: 트렌디한 패션에 집중, 클래식 스타일 소외
                - **높은 재고 회전율**: 자원 낭비와 과잉 생산 가능성
                """)

            # Opportunities 섹션
            with col1:
                st.subheader("Opportunities")
                st.markdown("""
                - **신흥 시장 진출**: 유럽, 스페인 외 신규 시장 확장 가능
                - **온라인 판매 강화**: 전자상거래 플랫폼 강화로 디지털 판매 확대
                """)

            # Threats 섹션
            with col2:
                st.subheader("Threats")
                st.markdown("""
                - **경쟁 심화**: H&M, GAP 등과의 치열한 경쟁
                - **경제적 불확실성**: 경기 불황과 공급망 문제로 인한 비용 상승 우려
                """)

            # 분석 요약
            st.markdown("""
            ---
            INDITEX는 빠른 트렌드 대응과 효율적인 공급망으로 강점을 유지하고 있음. SPA업계 특성상 과감한 물류, 온라인 매출 투자, 트렌드 대응 필요.
            """)

            st.title("Inditex (Zara) - Porter's 5 Forces Analysis")

            # Define the 5 Forces data in a structured format
            forces_data = {
                "산업 내 경쟁 강도": [
                    "높음: H&M, UNIQLO, GAP 등과 치열한 경쟁",
                    "트렌디한 디자인, 저렴한 가격, 빠른 생산 주기로 경쟁 심화"
                ],
                "신규 진입자의 위협": [
                    "중간: Inditex의 수직 통합 모델과 글로벌 운영으로 진입 장벽이 있음",
                    "그러나 Shein 등 온라인 전용 패스트 패션 기업이 위협 요소로 등장"
                ],
                "대체제의 위협": [
                    "중간에서 높음: 중고 의류, 지속가능 패션, 렌탈 서비스 등이 대체제로 부상",
                    "지속가능성에 대한 소비자 관심 증가로 대체제 위협 상승"
                ],
                "공급자의 협상력": [
                    "낮음: 수직 통합 모델로 많은 생산 과정을 직접 통제",
                    "대규모 주문량으로 외부 공급업체에 강한 협상력 행사 가능"
                ],
                "구매자의 협상력": [
                    "높음: 소비자는 선택지가 많고 브랜드 전환 비용이 낮음",
                    "온라인 쇼핑의 발달로 구매자의 협상력 강화"
                ]
            }

            # Display each force with its description
            st.markdown("""
                <style>
                .quadrant {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 20px;
                    justify-content: center;
                    text-align: center;
                }
                .quadrant-item {
                    background-color: #f8f8f8;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                    width: 90%;
                    margin-bottom: 15px;
                }
                .quadrant-title {
                    font-size: 1.5em;
                    font-weight: bold;
                    color: #333;
                    margin-bottom: 10px;
                }
                .quadrant-content {
                    color: #555;
                }
                </style>
            """, unsafe_allow_html=True)

            st.markdown('<div class="quadrant">', unsafe_allow_html=True)
            for force, description in forces_data.items():
                st.markdown(f"""
                    <div class="quadrant-item">
                        <div class="quadrant-title">{force}</div>
                        <div class="quadrant-content">
                            {'<br>'.join(description)}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            def load_data():
                # INDITEX (Ticker: ITX.MC) & Madrid IBEX 35 (^IBEX) 데이터 가져오기
                end_date = datetime.date.today()
                inditex = yf.download("ITX.MC", start="2000-01-01", end=end_date, progress=False)['Close'].squeeze()
                ibex = yf.download("^IBEX", start="2000-01-01", end=end_date, progress=False)['Close'].squeeze()

                # 데이터 존재 여부 확인
                if inditex.empty or ibex.empty:
                    st.error("데이터 로드에 실패했습니다.")
                    return None

                # 필요 컬럼 선택 (종가만 사용) 및 인덱스를 데이터프레임으로 생성
                data = pd.DataFrame({
                    'Inditex': inditex,
                    'IBEX 35': ibex
                })

                return data

            # 데이터 로드
            data = load_data()

            # 데이터가 성공적으로 로드되었는지 확인
            if data is not None:
                # 데이터 시각화
                st.subheader("Inditex와 IBEX 35 지수 비교")
                st.line_chart(data)

                # 로그 스케일 옵션
                use_log = st.checkbox("로그 스케일로 보기")

                # 차트 그리기
                fig, ax = plt.subplots(figsize=(14, 7))
                if use_log:
                    ax.set_yscale('log')
                    
                data.plot(ax=ax)
                ax.set_title("Inditex vs IBEX 35 Index (2000 - Present)")
                ax.set_ylabel("Index Level")
                ax.set_xlabel("Date")
                st.pyplot(fig)
            else:
                st.write("데이터 로드에 실패했습니다. 다시 시도해 주세요.")


        elif selected_sub_menu == "AI전략":
            # 제목 설정
            st.title("Inditex 디지털 전환 및 AI 전략")
            st.image(r"C:\Users\USER\Desktop\presentation\zara_ai.png")
            # 섹션별 내용
            st.subheader("1. 주요 프로젝트")
            st.markdown("""
            - **INDITEX OPEN PLATFORM**: 온오프라인 통합 재고 관리 시스템 개발로 이윤 극대화
            - **디지털 투자**: 온라인 역량 강화에 10억 유로, 매장 디지털화에 17억 유로 투자
            - **글로벌 판매 네트워크 통합**: 59개국 오프라인 매장과 온라인 플랫폼 재고 통합으로 어디서나 동일 조건으로 제품 구매 가능
            - **RFID 시스템 도입**: 실시간 재고 추적과 관리를 위한 RFID 기술 도입
            """)

            st.subheader("2. 소비자 경험 개선")
            st.markdown("""
            - **옴니채널 서비스**: 'Store Mode'로 제품 탐색부터 구매까지 끊김 없는 경험 제공
            - **SNS 활용**: Instagram 등 SNS에서 제품 확인 및 구매 사이트로 직접 연결 가능
            - **오프라인 매장 체험형 공간화**: 최신 트렌드를 체험할 수 있는 프리미엄 공간으로 매장 전환
            """)

            st.subheader("3. AI 활용")
            st.markdown("""
            - **수요 예측 및 재고 관리**: AI를 통해 고객 선호도를 파악하고 재고를 최적화
            - **개인화된 추천 시스템**: 고객의 구매 이력과 선호도를 분석하여 맞춤형 제품을 추천
            """)

            st.markdown("---")
            st.markdown("Inditex는 AI와 디지털 전환을 중심으로 한 HORIZON 전략 활용, 고객 경험과 운영 효율성을 강화하며 시장에서의 경쟁 우위를 유지")


        elif selected_sub_menu == "결론":
            st.subheader("ZARA와 유니클로 비교")

            st.markdown('<div class="comparison-section">', unsafe_allow_html=True)

            # 1. 제품 전략
            st.subheader("1. 제품 전략")
            st.markdown("""
                **ZARA**  
                - 최신 트렌드를 빠르게 반영하여 젊은층을 타겟팅.
                - 다양한 디자인 제공과 빠른 제품 회전율을 특징으로 함.

                **유니클로**  
                - 기본적이고 기능성을 강조하며 모든 연령층을 타겟팅.
                - 히트텍, 에어리즘 등 기능성 의류에 중점.
                - 장기간 판매되는 기본 제품들이 많음.
            """)

            # 2. 공급망
            st.subheader("2. 공급망")
            st.markdown("""
                - **SPA 기업**으로서 ZARA와 유니클로 모두 생산부터 소비까지 통합 관리하는 구조를 채택.
                
                **ZARA**  
                - 자체 제조 공장을 통해 통합 관리를 하며 생산 및 공급망을 직속 관리함.
                
                **유니클로**  
                - 파트너형 아웃소싱을 통해 장기 계약을 맺고 있으며, 주요 생산 활동을 외부 파트너와 협력하여 운영함.
            """)

            # 3. 판매처
            st.subheader("3. 판매처")
            st.markdown("""
                **유니클로**  
                - 아시아(특히 중국) 시장에서의 매출이 전체 성장을 주도.
                - 온오프라인 통합을 강화하는 옴니채널 전략을 추구.

                **ZARA**  
                - 비효율적인 오프라인 매장을 줄이고 온라인 매출에 집중하는 전략을 강화.
                - 현재 전체 매출의 약 25%가 온라인을 통해 발생.
            """)

            st.markdown('</div>', unsafe_allow_html=True)


    elif selected_brand == "GAP":
        if selected_sub_menu == "기업개요":
            # 좌우 레이아웃 구성
            col1, col2 = st.columns([1, 2])

            # 왼쪽에 로고 표시
            with col1:
                st.image(r"C:\Users\USER\Desktop\presentation\gap.png", caption="GAP", use_column_width=True)

            # 오른쪽에 기업 정보 요약
            with col2:
                st.subheader("GAP 기업 개요")
                st.markdown("""
                - **설립**: 1969년 8월 21일
                - **창업자**: 도널드 피셔(Donald Fisher)와 도리스 피셔(Doris Fisher) 부부
                - **본사 위치**: 미국 캘리포니아주 샌프란시스코
                - **주요 브랜드**: GAP, Old Navy, Banana Republic, Athleta
                """)

                st.subheader("재무 현황 (2023년 말 기준)")
                st.markdown("""
                - **연간 매출**: 148억 8900만 달러
                - **연간 영업이익**: 5억 200만 달러
                - **시가총액**: 87억 4135만 달러 (2024년 8월 기준)
                - **전 세계 매장 수**: 3,352개
                - **Fortune 500 순위**: 278위 (2024년 기준)
                """)

            # GAP 주요 브랜드 소개 데이터
            data = {
                "브랜드": ["GAP", "Old Navy", "Banana Republic", "Athleta"],
                "특징": [
                    "- GAP의 대표 브랜드\n- 클래식하고 캐주얼한 스타일의 의류",
                    "- 저렴한 가격대의 패밀리 캐주얼 브랜드\n- 매장 수: 약 1,200개 (2020년 기준)\n- 확장 계획: 30~40개의 신규 매장 오픈 예정",
                    "- 성인을 타겟으로 한 비즈니스, 캐주얼 프리미엄 브랜드\n- 구조조정: 북미 지역에서 130개 매장 폐점 계획 (2020년 발표)",
                    "- 요가, 피트니스 등 여성을 위한 활동적인 라이프스타일 의류\n- 매장 수: 약 200개 (2020년 기준)\n- 확장 계획: 300개 정도로 매장 수 확대 예정"
                ]
            }

            # 데이터프레임 생성
            df = pd.DataFrame(data)

            # Streamlit에 표 형태로 출력
            st.title("GAP 주요 브랜드 소개")
            st.table(df)


        elif selected_sub_menu == "연혁":
                        # 스타일 설정
            st.markdown("""
                <style>
                    .timeline {
                        font-family: Arial, sans-serif;
                        padding: 10px;
                    }
                    .timeline-item {
                        margin-left: 20px;
                        padding: 10px;
                        border-top: 1px dashed #ccc;
                        display: flex;
                        align-items: center;
                    }
                    .timeline-date {
                        font-weight: bold;
                        color: #333;
                        min-width: 100px;
                    }
                    .timeline-text {
                        flex-grow: 1;
                        color: #333;
                    }
                    .timeline-image {
                        margin-left: 15px;
                        width: 100px;
                        height: auto;
                    }
                </style>
            """, unsafe_allow_html=True)

            # 타임라인 내용
            timeline_content = [
                {
                    "date": "1969년",
                    "text": "도널드 피셔와 도리스 피셔 부부가 샌프란시스코에 첫 GAP 매장 오픈\n- Levi's 청바지와 LP 음반 판매로 시작",
                    "image": r"C:\Users\USER\Desktop\presentation\gap1969.jpg",
                    "link": "https://www.example.com"
                },
                {
                    "date": "1970년대",
                    "text": "빠른 확장으로 1973년까지 25개 이상의 매장 보유\n- 자체 브랜드 의류 판매 시작",
                    "image": r"C:\Users\USER\Desktop\presentation\gap1972.jpg",
                    "link": None
                },
                {
                    "date": "1976년",
                    "text": "기업 공개(IPO) 실시, 추가 확장을 위한 자본 확보",
                    "image": r"C:\Users\USER\Desktop\presentation\gap1976.jpg",
                    "link": None
                },
                {
                    "date": "1980년대",
                    "text": "Levi's 소매업체에서 자체 의류 브랜드 출시로 전환\n- 1983년 바나나 리퍼블릭(Banana Republic) 인수",
                    "image": r"C:\Users\USER\Desktop\presentation\gap1983.jpg",
                    "link": None
                },
                {
                    "date": "1994년",
                    "text": "저가 브랜드 올드 네이비(Old Navy) 런칭",
                    "image": r"C:\Users\USER\Desktop\presentation\gap1994.jpg",
                    "link": None
                },
                {
                    "date": "2000년대 초반",
                    "text": "소비자 선호도 변화와 패스트 패션 브랜드와의 경쟁으로 어려움 직면\n- 매장 폐쇄 및 운영 재구성 시작",
                    "image": None,
                    "link": None
                },
                {
                    "date": "2008년",
                    "text": "여성 스포츠 및 활동복 브랜드 애슬레타(Athleta) 인수",
                    "image": None,
                    "link": None
                },
                {
                    "date": "2010년대",
                    "text": "전자상거래 및 디지털 전략 강화\n- 지속 가능성 및 윤리적 생산에 대한 관심 증가",
                    "image": None,
                    "link": None
                },
                {
                    "date": "2023년",
                    "text": "현재 CEO 리처드딕슨 취임",
                    "image": r"C:\Users\USER\Desktop\presentation\gap2023.jpg",
                    "link": None
                }
            ]

            # GAP 요약 설명
            st.markdown("GAP은 초기 청바지 전문점에서 시작하여 글로벌 패션 기업으로 성장했습니다. 시대의 변화에 따라 다양한 도전에 직면했지만, 브랜드 다각화와 디지털 전환 등을 통해 적응해 왔습니다. 최근에는 지속 가능성과 온라인 비즈니스 강화에 주력하고 있습니다.")

            # 타임라인 표시
            st.markdown("<div class='timeline'>", unsafe_allow_html=True)
            for item in timeline_content:
                st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)
                st.markdown(f"<span class='timeline-date'>{item['date']}</span>", unsafe_allow_html=True)
                st.markdown(f"<span class='timeline-text'>{item['text']}</span>", unsafe_allow_html=True)
                
                # 로컬 이미지가 있는 경우 표시
                if item["image"]:
                    st.image(item["image"], width=100)  # 로컬 이미지 표시, 너비 조정 가능
                
                st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        elif selected_sub_menu == "재무":
            # 데이터 준비
            data_sales = {
                "year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
                "sales": [14664, 14549, 15651, 16148, 16435, 15797, 15516, 15855, 16580, 16383, 13800, 16670, 15616, 14889],
                "stores": [3063, 3026, 3052, 3090, 3183, 3159, 3183, 3113, 3143, 3156, 2950, 2835, 2685, 2562]
            }

            data_income = {
                "year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
                "net_income": [1204, 833, 1135, 1280, 1262, 920, 676, 848, 1003, 351, -665, 256, -202, 502],
                "stores": [3063, 3026, 3052, 3090, 3183, 3159, 3183, 3113, 3143, 3156, 2950, 2835, 2685, 2562]
            }

            # 백만 달러(millions)에서 십억 달러(billions)로 변환
            df_sales = pd.DataFrame(data_sales)
            df_income = pd.DataFrame(data_income)
            df_sales["sales"] = df_sales["sales"] / 1000  # Millions to Billions
            df_income["net_income"] = df_income["net_income"] / 1000  # Millions to Billions

            # Streamlit 앱 제목
            st.title("GAP Financial Data")

            # 차트 1 - Sales와 Store Count
            fig1 = go.Figure()

            # Sales는 막대그래프
            fig1.add_trace(go.Bar(
                x=df_sales["year"],
                y=df_sales["sales"],
                name="Sales (Billions of Dollar)",
                marker_color="skyblue"
            ))

            # Store Count는 꺾은선 그래프, 오른쪽 축
            fig1.add_trace(go.Scatter(
                x=df_sales["year"],
                y=df_sales["stores"],
                name="Store Count",
                mode="lines+markers",
                marker_color="green",
                yaxis="y2"
            ))

            # 레이아웃 설정
            fig1.update_layout(
                title="Sales and Store Count Over Time",
                xaxis_title="Year",
                yaxis_title="Sales (Billions of Dollar)",
                yaxis2=dict(
                    title="Store Count",
                    overlaying="y",
                    side="right"
                ),
                legend=dict(x=0.01, y=0.99)
            )

            # 차트 출력
            st.plotly_chart(fig1)

            # 차트 2 - Net Income와 Store Count
            fig2 = go.Figure()

            # Net Income는 막대그래프
            fig2.add_trace(go.Bar(
                x=df_income["year"],
                y=df_income["net_income"],
                name="Net Income (Billions of Dollar)",
                marker_color="salmon"
            ))

            # Store Count는 꺾은선 그래프, 오른쪽 축
            fig2.add_trace(go.Scatter(
                x=df_income["year"],
                y=df_income["stores"],
                name="Store Count",
                mode="lines+markers",
                marker_color="green",
                yaxis="y2"
            ))

            # 레이아웃 설정
            fig2.update_layout(
                title="Net Income and Store Count Over Time",
                xaxis_title="Year",
                yaxis_title="Net Income (Billions of Dollar)",
                yaxis2=dict(
                    title="Store Count",
                    overlaying="y",
                    side="right"
                ),
                legend=dict(x=0.01, y=0.99)
            )
            # 차트 출력
            st.plotly_chart(fig2)

            # 매장수가 급감한 것이 팩트인가?
            st.markdown("[의류브랜드 GAP이 향후 2년 간 230개 점포를 폐쇄한다](https://www.huffingtonpost.kr/news/articleView.html?idxno=80596)")

            # 데이터 준비 및 변환
            data = {
                "year": [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
                "United States": [11368, 12194, 12531, 12672, 12213, 11989, 12568, 13340, 13398, 11650, 14117, 13201, 12967],
                "Canada": [1007, 1095, 1128, 1137, 1047, 1084, 1173, 1193, 1153, 972, 1252, 1236, 1221],
                "Other regions": [135, 182, 201, 207, 219, 210, 210, 211, 209, 139, 231, 298, 701],
                "Europe": [863, 870, 891, 917, 797, 689, 641, 603, 539, 329, 340, 209, None],
                "Asia": [1176, 1310, 1397, 1502, 1521, 1544, 1263, 1233, 1084, 710, 730, 672, None]
            }

            # 데이터프레임 생성 및 수치 변환 (millions to billions)
            df = pd.DataFrame(data)
            df[["United States", "Canada", "Other regions", "Europe", "Asia"]] = df[["United States", "Canada", "Other regions", "Europe", "Asia"]] / 1000

            # Streamlit 앱 제목
            st.title("GAP Regional Revenue (Billions of Dollar)")

            # 누적 막대 그래프 생성
            fig = go.Figure()

            # 각 지역별 데이터를 막대 그래프에 추가
            regions = ["United States", "Canada", "Other regions", "Europe", "Asia"]
            colors = ["skyblue", "lightgreen", "orange", "lightcoral", "purple"]

            for i, region in enumerate(regions):
                fig.add_trace(go.Bar(
                    x=df["year"],
                    y=df[region],
                    name=region,
                    marker_color=colors[i]
                ))

            # 레이아웃 설정
            fig.update_layout(
                title="GAP Revenue by Region Over Time",
                xaxis_title="Year",
                yaxis_title="Revenue (Billions of Dollar)",
                barmode="stack",
                legend=dict(x=0.01, y=0.99)
            )

            # 차트 출력
            st.plotly_chart(fig)


        elif selected_sub_menu == "비즈니스 분석":
            # 제목 설정
            st.title("GAP SWOT Analysis")

            # 4분면 레이아웃 설정
            col1, col2 = st.columns(2)

            # Strengths 섹션
            with col1:
                st.subheader("Strengths")
                st.markdown("""
                - **강력한 브랜드 포트폴리오**: Gap, Old Navy, Banana Republic, Athleta 등 다양한 고객층을 타겟으로 함.
                - **글로벌 인지도**: 오랜 시간 동안 쌓아온 브랜드 신뢰도와 글로벌 인지도가 강점.
                - **오프라인 매장 네트워크**: 미국과 주요 국가에 걸쳐 있는 강력한 오프라인 채널.
                """)

            # Weaknesses 섹션
            with col2:
                st.subheader("Weaknesses")
                st.markdown("""
                - **트렌드 반영 속도**: 패스트 패션 브랜드와 비교해 트렌드 반영 속도가 느림.
                - **할인 의존성**: 빈번한 할인 행사로 인해 브랜드 가치 하락 우려.
                - **비용 구조**: 오프라인 매장 운영에 따른 고정비가 높아 비용 효율성 저하.
                """)

            # Opportunities 섹션
            with col1:
                st.subheader("Opportunities")
                st.markdown("""
                - **전자상거래 성장**: 디지털 판매 강화 기회가 증가.
                - **ESG 및 지속 가능성**: 친환경 및 지속 가능한 패션에 대한 수요 증가로 브랜드 이미지 개선 가능.
                - **글로벌 시장 확장**: 아시아 및 신흥 시장에서의 수요 증가로 추가 시장 진입 기회.
                """)

            # Threats 섹션
            with col2:
                st.subheader("Threats")
                st.markdown("""
                - **경쟁 심화**: ZARA, H&M 등 패스트 패션 브랜드와의 치열한 경쟁.
                - **원자재 가격 변동**: 원자재 가격 상승 시 수익성 악화 가능성.
                - **경제 불확실성**: 경기 불황으로 인한 소비 둔화 위험.
                """)

            # 분석 요약
            st.markdown("""
            ---
            GAP은 여전히 미국, 해외에서 높은 인지도를 갖추고 있으나, H&M, ZARA 등 경쟁업체의 대응에 어려움을 겪고 있음
            """)

            # Porter’s 5 Forces 분석
            st.title("GAP - Porter's 5 Forces Analysis")

            # Define the 5 Forces data in a structured format
            forces_data = {
                "기존 경쟁자 간 경쟁": [
                    "의류 업계 내 H&M, Zara, Uniqlo 등과의 치열한 경쟁.",
                    "고객의 브랜드 전환 비용이 낮아 경쟁이 격화됨."
                ],
                "신규 진입자의 위협": [
                    "패션 산업 진입 장벽이 낮아 신생 브랜드가 지속적으로 등장.",
                    "Gap의 브랜드 인지도와 규모는 일정한 보호 장벽을 제공."
                ],
                "대체재의 위협": [
                    "의류는 필수 소비재이지만 다양한 스타일과 브랜드가 대체제로 작용.",
                    "소규모 로컬 브랜드와 맞춤형 의류는 잠재적 위협이 됨."
                ],
                "고객의 협상력": [
                    "고객은 다양한 선택지를 가지고 가격에 민감하게 반응.",
                    "충성도가 낮아 GAP은 고객 만족도 유지를 위해 지속적인 노력 필요."
                ],
                "공급자의 협상력": [
                    "다양한 국가에 공급망을 구축하여 특정 공급자에 대한 의존도 낮춤.",
                    "공급자의 협상력 약화로 원가 절감과 안정적 공급 가능."
                ]
            }

            # Streamlit layout styling
            st.markdown("""
                <style>
                .quadrant {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 20px;
                    justify-content: center;
                    text-align: center;
                }
                .quadrant-item {
                    background-color: #f8f8f8;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                    width: 90%;
                    margin-bottom: 15px;
                }
                .quadrant-title {
                    font-size: 1.5em;
                    font-weight: bold;
                    color: #333;
                    margin-bottom: 10px;
                }
                .quadrant-content {
                    color: #555;
                }
                </style>
            """, unsafe_allow_html=True)

            # Display the 5 Forces analysis in shaded boxes
            for force, points in forces_data.items():
                st.markdown(f"<div class='quadrant-item'><div class='quadrant-title'>{force}</div>", unsafe_allow_html=True)
                st.markdown("<div class='quadrant-content'><ul>", unsafe_allow_html=True)
                for point in points:
                    st.markdown(f"<li>{point}</li>", unsafe_allow_html=True)
                st.markdown("</ul></div></div>", unsafe_allow_html=True)

            # 데이터 로드 함수
            def load_data():
                # GAP (Ticker: GPS) & S&P 500 Index (^GSPC) 데이터 가져오기
                end_date = datetime.date.today()
                gap = yf.download("GPS", start="2000-01-01", end=end_date, progress=False)['Close']
                sp500 = yf.download("^GSPC", start="2000-01-01", end=end_date, progress=False)['Close']

                # 데이터가 정상적으로 로드되었는지 확인
                if gap.empty or sp500.empty:
                    return None

                # DataFrame으로 종가 데이터 생성
                data = pd.DataFrame({
                    'GAP': gap,
                    'S&P 500': sp500
                })

                return data

            # 데이터 로드
            data = load_data()

            # 데이터가 성공적으로 로드되었는지 확인
            if data is not None:
                # 데이터 시각화
                st.subheader("GAP과 S&P 500 지수 비교")
                st.line_chart(data)

                # 로그 스케일 옵션
                use_log = st.checkbox("로그 스케일로 보기")

                # 차트 그리기
                fig, ax = plt.subplots(figsize=(14, 7))
                if use_log:
                    ax.set_yscale('log')
                    
                data.plot(ax=ax)
                ax.set_title("GAP vs S&P 500 Index (2000 - Present)")
                ax.set_ylabel("Index Level")
                ax.set_xlabel("Date")
                st.pyplot(fig)
            else:
                st.error("데이터 로드에 실패했습니다. 다시 시도해 주세요.")



        elif selected_sub_menu == "AI전략":
            # 제목 설정
            st.title("GAP 디지털 전환 개요")

            # 디지털 전환 목표
            st.subheader("디지털 전환 목표")
            st.markdown("""
            - **온라인과 오프라인 매장의 통합**
            - **고객 경험 향상**
            - **온라인 매출 비중 확대**
            """)

            # 주요 전략 및 투자
            st.subheader("주요 전략 및 투자")
            st.markdown("""
            - **Microsoft Azure 클라우드 도입**
            - **모바일 및 디지털 역량 강화**
            - **공급망 현대화**
            - **매장 내 경험 개선**
            - **새로운 쇼핑 방식 제공**
            - **중앙 집중식 데이터 플랫폼 구축**: Azure를 기반으로 개인화된 쇼핑 경험 제공
            - **AI 기술 활용**:
                - TrueFit와 파트너십을 통한 AI 기반 사이즈 추천 제공
                - Drapr 인수로 가상 피팅룸 기술 도입
            - **Microsoft 365 솔루션 도입**: 글로벌 인력의 협업 강화, 브랜드 및 채널 간 효율적인 작업 지원
            """)

            # 디지털 혁신 성과
            st.subheader("디지털 혁신 성과")
            st.markdown("""
            - **온라인 판매 성장**: 2020년 온라인 매출이 54% 증가하며, 총 매출의 45% ($6 billion) 차지
            - **오프라인 매장 조정**: 영국 및 아일랜드 오프라인 매장 폐쇄, 온라인 비즈니스에 집중
            - **고객 경험 개선**:
                - AI 기반 사이즈 추천 도입으로 반품률 감소
                - 가상 피팅 기술로 구매 결정 지원
            - **운영 효율성 향상**:
                - Azure 클라우드를 통한 확장성 및 유연성 확보
                - 데이터 기반 의사결정 강화
            """)

            # 요약
            st.markdown("---")
            st.markdown("""
            GAP의 디지털 전환 전략은 클라우드 기술, AI, 데이터 분석을 중심으로 진행되고 있으며, 온라인과 오프라인의 통합, 고객 경험 개선, 운영 효율성 향상에 초점을 맞추고 있습니다.
            특히 AI 기술을 활용한 사이즈 추천과 가상 피팅 서비스는 온라인 쇼핑의 주요 문제점을 해결하고 고객 만족도를 높이는 데 기여하고 있습니다.
            """)

        elif selected_sub_menu == "결론":

            st.image("https://files.oaiusercontent.com/file-CzNkiZvxjU2Njo9DbcDams7P?se=2024-11-01T09%3A34%3A59Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3Dbb418c1a-7b1b-4e3c-8b7a-42f12d388d8f.webp&sig=7h1hRcdYvwqHuj9GhYuNsrSNuyufnIg3Lz2haCmKmqY%3D")

            st.title("SPA(Specialty store retailer of Private label Apparel) 기업의 의미")

            st.markdown("""
            - **자체 브랜드 제품 생산**: 디자인, 생산, 유통, 판매까지 모든 과정을 기업이 자체적으로 관리하여 브랜드 통일성을 유지
            - **빠른 트렌드 반영**: 최신 패션 트렌드를 신속하게 제품에 반영하여 짧은 주기로 신상품 출시
            - **비용 절감**: 중간 유통 과정을 없애고 직접 운영하여 비용을 낮추고 가격 경쟁력 확보
            - **재고 관리 최적화**: 수요 예측과 빠른 재고 회전율로 재고 비용을 최소화
            - **온·오프라인 채널 통합**: 온라인 매출 확대 및 옴니채널 전략을 통해 다양한 소비자 접점 확보

            SPA 모델은 빠른 패션 순환과 가격 경쟁력을 통해 소비자의 변화하는 요구에 민첩하게 대응하는 것을 목표로 함.
            """)

                        # 타이틀과 설명
            st.title("Fast Retailing, Inditex, GAP 2023 비교")
            st.markdown("2023년 기준으로 Fast Retailing (UNIQLO), Inditex (ZARA), GAP Inc.의 주요 지표 비교")

            # HTML로 커스텀 스타일 적용한 표
            st.markdown("""
                <style>
                    .comparison-table {
                        width: 100%;
                        border-collapse: collapse;
                        font-family: Arial, sans-serif;
                        margin-top: 20px;
                    }
                    .comparison-table th {
                        background-color: #4CAF50;
                        color: white;
                        padding: 10px;
                    }
                    .comparison-table td {
                        padding: 10px;
                        text-align: center;
                        border-bottom: 1px solid #ddd;
                    }
                    .comparison-table tr:nth-child(even) {
                        background-color: #f2f2f2;
                    }
                </style>
                
                <table class="comparison-table">
                    <tr>
                        <th>지표</th>
                        <th>Fast Retailing (UNIQLO)</th>
                        <th>Inditex (ZARA)</th>
                        <th>GAP Inc.</th>
                    </tr>
                    <tr>
                        <td>매출</td>
                        <td>2조 7,665억 엔 (약 18.3조 원)</td>
                        <td>359억 유로 (약 51.3조 원)</td>
                        <td>140억 달러 (약 18.7조 원)</td>
                    </tr>
                    <tr>
                        <td>매장 수</td>
                        <td>3,747개 (UNIQLO)</td>
                        <td>5,692개</td>
                        <td>2,743개</td>
                    </tr>
                    <tr>
                        <td>직원 수</td>
                        <td>56,000명 (UNIQLO)</td>
                        <td>160,000명</td>
                        <td>95,000명</td>
                    </tr>
                    <tr>
                        <td>브랜드 지위</td>
                        <td>글로벌 SPA 브랜드로서 아시아 시장에서 강세</td>
                        <td>글로벌 최대 패스트 패션 기업</td>
                        <td>미국 중심의 캐주얼 의류 브랜드</td>
                    </tr>
                </table>
            """, unsafe_allow_html=True)

            st.title("SPA 브랜드들의 디지털 전환과 성장 전략 비교")
            st.markdown("### UNIQLO, ZARA, GAP의 성장 전략과 방향성 비교")
            st.markdown("""
            - **공통 전략:**  
            UNIQLO와 ZARA는 재고비용 최소화와 트렌드 및 수요 예측을 통해 수익성을 극대화하는 전략을 구사.
            AI, RFID 같은 정보화 기술을 도입하고, 구글 등 데이터 기업과 협력하며 온라인 매출 확대에 주력하여 수익성 강화에 성공.

            - **ZARA:**  
            - 유럽과 미국 등 글로벌 시장에 성공적으로 진출하여 최신 패션 트렌드를 반영한 제품을 제공.
            - 비용이 많이 드는 매장을 과감히 정리하고, 트렌드를 반영한 빠른 제품 출시로 높은 매출과 이익을 기록.

            - **UNIQLO:**  
            - 주로 아시아권에 진출해 있으며, 기능성과 품질을 강조한 제품을 통해 성장.
            - 일본 특유의 기능성 의류를 제공하는 전략으로 ZARA에 비해 매출은 적지만 꾸준히 성장.

            - **GAP:**  
            - 비용 절감과 온라인 매출 확대에 힘쓰며 SPA 모델을 유지했지만, 2010년대 들어 대중적인 아메리칸 이미지를 유지하다가 최신 트렌드에 반응하지 못함.
            - 디지털 전환에도 불구하고 트렌드를 선도하지 못해 어려움을 겪음.
            """)
            # 핵심 요점을 강조하여 표시
            st.markdown("""
            <div style="border: 2px solid #4CAF50; padding: 15px; border-radius: 10px; background-color: #f9f9f9;">
                <strong style="font-size: 1.2em; color: #333;">핵심 요점:</strong>  
                <p style="font-size: 1.1em;">
                AI와 디지털 기술 도입은 중요한 요소지만, 기업의 본질을 잃지 않으면서도 시대의 흐름을 반영하는 것이 가장 중요한 성공 요소.
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.title("The end")

