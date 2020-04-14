import xbmc,xbmcgui,xbmcaddon
import os, glob

xbmc.sleep(1000)
VisbleWindows = xbmc.getCondVisibility('[Window.IsActive(10700) | Window.IsActive(10702)]')
VisiblePVR = xbmc.getCondVisibility('!Pvr.IsPlayingTv + System.HasPVRAddon')

pvr_toggle_off = '{"jsonrpc": "2.0", "method": "Addons.SetAddonEnabled", "params": ' \
                         '{"addonid": "pvr.iptvsimple", "enabled": false}, "id": 1}'
pvr_toggle_on = '{"jsonrpc": "2.0", "method": "Addons.SetAddonEnabled", "params": ' \
                        '{"addonid": "pvr.iptvsimple", "enabled": true}, "id": 1}'

while not VisbleWindows:
    VisbleWindows = xbmc.getCondVisibility('[Window.IsActive(10700) | Window.IsActive(10702)]')
    if VisiblePVR and VisbleWindows:
        xbmc.sleep(1000)
        xbmc.executeJSONRPC(pvr_toggle_off)
        xbmc.sleep(1000)
        xbmc.executeJSONRPC(pvr_toggle_on)
        if xbmcaddon.Addon().getSetting(id='delete_logs') == 'true':
            fileList = glob.glob('/storage/.kodi/temp/kodi_crash*.*')
            for filePath in fileList:
                os.remove(filePath)
        break
    xbmc.sleep(1000)
else:
    if VisiblePVR:
        xbmc.sleep(1000)
        xbmc.executeJSONRPC(pvr_toggle_off)
        xbmc.sleep(1000)
        xbmc.executeJSONRPC(pvr_toggle_on)
        if xbmcaddon.Addon().getSetting(id='delete_logs') == 'true':
            fileList = glob.glob('/storage/.kodi/temp/kodi_crash*.*')
            for filePath in fileList:
                os.remove(filePath)
    else:
        xbmcgui.Dialog().dialog.ok('There are no PVR Clients installed', 'Please install to use PVR.')
