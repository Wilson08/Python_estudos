@dataclass
class StarWarsMovie:
   title: str
   episode_id: int
   opening_crawl: str
   director: str
   producer: str
   release_date: datetime
   characters: List[str]
   planets: List[str]
   starships: List[str]
   vehicles: List[str]
   species: List[str]
   created: datetime
   edited: datetime
   url: str