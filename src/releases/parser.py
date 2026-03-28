
class Parser:
    def __init__(self, dictionary: list[dict]) -> None:
        self.dictionary: list[dict] = dictionary
    
    def parse(self) -> dict:
        releases = {}
        for r in self.dictionary:
            self._add_release(
                releases = releases,
                version  = self._get_release_version(r),
                name     = r.get('name', "err!"),
                assets   = self._get_assets(r.get('assets', {}))
            )
        return releases
    
    def _add_release(self, releases: dict, version: int | float, name: str, assets: dict) -> None:
        releases[version] = {'name': name, 'assets': assets}
    
    ## assets
    def _get_assets(self, assets: dict) -> dict:
        parsed = {}
        for res in assets:
            res_name = res.get('name')
            res_url = res.get('browser_download_url')
            
            if res_name != None and res_url != None:
                parsed[res_name] = res_url
        
        return parsed
    
    ## version
    def _get_tag_name(self, release_data: dict) -> str:
        return release_data.get('tag_name', 'err!')
            
    def _get_release_version(self, release_data: dict) -> float | int:
        tag_name = self._get_tag_name(release_data)
        try: 
            return Parser.get_version_number(tag_name)
        except ValueError: 
            return int('000' +  self._get_strint_from_str(tag_name))
    
    def _get_strint_from_str(self, string: str) -> str:
        return ''.join([str(ord(c)) for c in string])
    
    @staticmethod
    def _normalize_number(x):
        return int(x) if x % 1 == 0 else float(x)
    
    @staticmethod
    def get_version_number(string: str) -> int | float:
        if string[0] == 'v':
            string = string[1:]
        return Parser._normalize_number(float(string))