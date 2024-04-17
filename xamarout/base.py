class XamarinBase:
    def __init__(self, filepath=None, manifest_path=None) -> None:
        self.filepath = filepath
        self.manifest_path = manifest_path
        self._manifest = None
        if filepath is not None:
            self.from_file(filepath)
    
    def from_file(self, filepath:str):
        "Read bytes from <filepath> and attempt to apply file structre"
        with open(filepath, "rb") as f:
            return self.from_bytes(f.read())
    
    def from_bytes(self, data:bytes):
        pass
