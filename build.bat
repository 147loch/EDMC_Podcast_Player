mkdir dist\EDMC_Podcast_Player\downloads

copy /Y *.py dist\EDMC_Podcast_Player
copy /Y downloads\* dist\EDMC_Podcast_Player\downloads

explorer dist\EDMC_Podcast_Player\

rem cd "%LOCALAPPDATA%\EDMarketConnector\plugins"
