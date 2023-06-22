import flet as ft
import webbrowser


__VERSION__ = "1.0.0"
__AUTHOR__ = "AmirTP"
__ID__ = "@Amirhossein_tp"
__CONTENT__ = f"""
**Version: {__VERSION__}**

**Author: [{__AUTHOR__} ({__ID__})](https://t.me/Amirhossein_tp)**

**Our Channel: [MicrosoftRewardIran Telegram](https://t.me/microsoftrewardiran)**

**More Info: [Telegram Bot](http://t.me/MyMoneyMindBot)**

### **Use it at your own risk, Microsoft may ban your account!**

### Your support will be much appreciated

  - **BTC (BTC network):** bc1qlg5leeney6wdc52ut4739nv9s8gggwmk5r58zq
  - **ETH (ERC20):** 0x2898De763060E87A4408Ed4132dDa235c9D2E903
  - **TRX (TRC20):** TJY748EgEhEroT3qiZvAessgeeMhwwudtq
"""

__LICENSE__ = """
Copyright (c) 2023 AmirTP
"""


class About(ft.UserControl):
    def __init__(self, parent, page: ft.Page):
        from .app_layout import UserInterface
        super().__init__()
        self.parent: UserInterface = parent
        self.page = page
        self.ui()
        self.page.update()
    
    def ui(self):
        self.title = ft.Row(
            controls=[
                ft.Text(
                    value="About",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    text_align="center",
                    expand=True,
                ),
            ]
        )
        self.content = ft.Markdown(
            value=__CONTENT__,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: webbrowser.open(e.data)
        )
        self.license_label = ft.Row([ft.Text("LICENSE", size=18, weight=ft.FontWeight.BOLD, text_align="center", expand=True)])
        self.license = ft.Markdown(__LICENSE__)
        self.about_card = ft.Card(
            expand=True,
            content=ft.Container(
                margin=ft.margin.all(15),
                alignment=ft.alignment.top_center,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        self.title,
                        ft.Divider(),
                        self.content
                    ]
                )
            )
        )
    
    def build(self):
        return ft.Container(
            margin=ft.margin.all(25),
            alignment=ft.alignment.top_center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment="stretch",
                controls=[
                    ft.Row(
                        controls=[self.about_card],
                        alignment="center"
                    ),
                ],
            ),
        )
        