DEFAULT_STYLE = "default"

class State():
    def __init__(self, name, root, styles):
        self.__name = name
        self.__root = root
        self.__styles = styles
        self.previous_window_size = self.get_window_size()
    
    def get_name(self):
        return self.__name
    
    def get_root(self):
        return self.__root
    
    def get_window_size(self):
        self.__root.update_idletasks()
        return self.__root.winfo_width(), self.__root.winfo_height()
    
    def has_window_size_changed(self):
        changed = self.previous_window_size != (self.get_window_size())
        
        if changed:
            self.previous_window_size = self.get_window_size()
        return changed
       
    
    def get_style(self, style_name = None):
        if (style_name is not None) and (style_name in self.__styles):
            return self.__styles[style_name]
        
        if DEFAULT_STYLE in self.__styles:
            return self.__styles[DEFAULT_STYLE]
        
        raise Exception("Default style does not exist")
