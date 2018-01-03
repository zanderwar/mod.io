import requests
BASE_PATH = "https://api.mod.io/v1"    

class Message:
    def __init__(self, **attrs):
        self.code = attrs.pop("code", None)
        self.message =attrs.pop("message", None)

class Error:
    def __init__(self, **attrs):
        self.code = attrs.pop("code", None)
        self.message = attrs.pop("message", None)
        self.errors = attrs.pop("errors", None)

class Image: #is used for Logo Object, Icon Object, Header Object, Avatar Object and Image Object
    def __init__(self, **attrs):
        self.filename = attrs.pop("filename", None)
        self.original = attrs.pop("original", None)

        if len(attrs) > 2:
            self.small = list(attrs.values())[2]
        if len(attrs) > 3:
            self.medium = list(attrs.values())[3]
        if len(attrs) > 4:
            self.large = list(attrs.values())[4]            

class GameActivity:
    def __init__(self, **attrs):
        self.id = attrs.pop("id", None)
        self.game_id = attrs.pop("game_id", None)
        self.user_id = attrs.pop("user_id", None)
        self.date_added = attrs.pop("date_added", None)
        self.event = attrs.pop("event", None)

        changes_list = list()
        changes = attrs.pop("changes", None)
        if not changes is None:
            for change in changes:
                changes_list.append(FieldChange(**change))

        self.changes = changes_list

class ModActivity:
    def __init__(self, **attrs):
        self.id = attrs.pop("id", None)
        self.mod_id = attrs.pop("mod_id", None)
        self.user_id = attrs.pop("user_id", None)
        self.date_added = attrs.pop("date_added", None)
        self.event = attrs.pop("event", None)
        
        changes_list = list()
        changes = attrs.pop("changes", None)
        if not changes is None:
            for change in changes:
                changes_list.append(FieldChange(**change))

        self.changes = changes_list

class FieldChange:
    def __init__(self, **attrs):
        self.field = attrs.pop("field", None)
        self.before = attrs.pop("before", None)
        self.after = attrs.pop("after", None)

class Comment:
    def __init__(self, **attrs):
        self.id = attrs.pop("id", None)
        self.mod_id = attrs.pop("mod_id", None)
        self.submitter = User(**attrs.pop("submitter", None))
        self.date_added = attrs.pop("date_added", None)
        self.reply_id = attrs.pop("reply_id", None)
        self.reply_position = attrs.pop("reply_position", None)
        self.karma = attrs.pop("karma", None)
        self.karma_guest = attrs.pop("karma_guest", None)
        self.content = attrs.pop("content", None)

class ModDependencies:
    def __init__(self, **attrs):
        self.mod_id = attrs.pop("mod_id", None)
        self.date_added = attrs.pop("date_added", None)

class ModFile:
    def __init__(self,**attrs):
        self.id = attrs.pop("id", None)
        self.mod_id = attrs.pop("mod_id", None)
        self.date_added = attrs.pop("date_added", None)
        self.date_scanned = attrs.pop("date_scanned", None)
        self.virus_status = attrs.pop("virus_status", None)
        self.virus_positive = attrs.pop("virus_positive", None)
        self.virustotal_hash = attrs.pop("virustotal_hash", None)
        self.filesize = attrs.pop("filesize", None)
        self.filehash = attrs.pop("filehash", None)["md5"]
        self.filename = attrs.pop("filename", None)
        self.version = attrs.pop("version", None)
        self.changelog = attrs.pop("changelog", None)

class ModMedia:
    def __init__(self, **attrs):
        self.youtube = attrs.pop("youtube", None)
        self.sketchfab = attrs.pop("sketchfab", None)

        images_list = list()
        images = attrs.pop("images", None)
        if not images is None:
            for image in images:
                images_list.append(Image(**image))

        self.images = images_list

class ModTag:
    def __init__(self, **attrs):
        self.name = attrs.pop("name", None)
        self.date_added = attrs.pop("date_added", None)

class GameTag:
    def __init__(self, **attrs):
        self.name = attrs.pop("name", None)
        self.type = attrs.pop("type", None)
        self.hidden = attrs.pop("hidden", None)
        self.tags = attrs.pop("tags", None)

class MetaData:
    def __init__(self, **attrs):
        self.key = attrs.pop("key", None)
        self.value = attrs.pop("value", None)

class RatingSummary:
    def __init__(self, **attrs):
        self.total_ratings = attrs.pop("total_ratings", None)
        self.positive_ratings = attrs.pop("positive_ratings", None)
        self.negative_ratings = attrs.pop("negative_ratings", None)
        self.percentage_positive = attrs.pop("percentage_positive", None)
        self.weighted_aggregate = attrs.pop("weighted_aggregate", None)
        self.display_text = attrs.pop("display_text", None)

class TeamMember:
    def __init__(self, **attrs):
        self.id = attrs.pop("id", None)
        self.user = User(**attrs.pop("user", None))
        self.level = attrs.pop("level", None)
        self.date_added = attrs.pop("date_added", None)
        self.position = attrs.pop("position", None)

class User:
    def __init__(self, **attrs):
        self.id = attrs.pop("id", None)
        self.name_id = attrs.pop("name_id", None)
        self.username = attrs.pop("username", None)
        self.date_online = attrs.pop("date_online", None)

        avatar = attrs.pop("avatar", None)

        if len(avatar.keys()) > 0:
            self.avatar = Image(**avatar)
        else:
            self.avatar = None

        self.timezone = attrs.pop("timezone", None)
        self.language = attrs.pop("language", None)
        self.profile_url = attrs.pop("profile_url", None)