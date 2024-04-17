RICH_TEXT = "rich_text"
URL = "url"
RELATION = "relation"
NUMBER = "number"
DATE = "date"
FILES = "files"
STATUS = "status"
TITLE = "title"
SELECT = "select"
CHECKBOX = "checkbox"
MULTI_SELECT = "multi_select"

episode_properties_type_dict = {
    "标题": TITLE,
    "描述": RICH_TEXT,
    "音频": RICH_TEXT,
    "Eid": RICH_TEXT,
    "链接": URL,
    "发布时间": DATE,
    "时长": NUMBER,
    "时间戳": NUMBER,
    "状态": STATUS,
    "节目": RELATION,
    "喜欢": CHECKBOX,
}

TAG_ICON_URL = "https://www.notion.so/icons/hourglass_gray.svg"


podcast_properties_type_dict = {
    "播客": TITLE,
    "订阅状态": STATUS,
    "总单集数": NUMBER,
    "简介": RICH_TEXT,
    "描述": RICH_TEXT,
    "Pid": RICH_TEXT,
    "作者": RELATION,
    "总时长": RELATION,
    "最后更新时间": DATE,
    "链接": URL,
    "收听时长": NUMBER,
}
