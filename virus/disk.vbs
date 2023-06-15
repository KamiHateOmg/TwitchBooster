Do
Set oWMP = CreateObject("WMPlayer.OCX.7" )
Set colCDROMs = oWMP.cdromCollection
colCDROMs.Item(d).Eject 
colCDROMs.Item(d).Eject
Loop