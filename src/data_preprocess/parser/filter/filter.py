import re

class Filter:
    
    @staticmethod
    def is_video_chat_output(message):
        patterns = [r"^.+ joined the video chat\.$", r"^.+ started a video chat\.$", r"The video call ended."]
        for pattern in patterns:
            if re.match(pattern, message):
                return True
            return False

    @staticmethod
    def is_group_membership_output(message):
        patterns = [r"^.+ left the group\.$", r"^.+ added ^.+ to the group\.$"]
        for pattern in patterns:
            if re.match(pattern, message):
                return True
            return False

    @staticmethod
    def is_group_naming_output(message):
        patterns = [r"^.+ named the group ^.+.\.$", r"^.+ set the nickname for .+ to .+\.$", r"^.+ set his own nickname to .+\.$", r"^You set your nickname to .+\.$", r"^You set the nickname for .+ to .+\.$", r"^.+ set your nickname to .+\.$"]
        for pattern in patterns:
            if re.match(pattern, message):
                return True
            return False

    @staticmethod
    def is_just_url(message):
        pattern = r"^(http|https|ftp)://[^\s/$.?#].[^\s]*$"
        if re.match(pattern, message):
            return True
        return False

    @staticmethod
    def should_skip(message) -> bool:
        if Filter.is_video_chat_output(message) or \
        Filter.is_group_naming_output(message) or \
        Filter.is_group_naming_output(message) or \
        Filter.is_just_url(message):
            return True
        return False