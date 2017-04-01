# -*- mode: python -*-

block_cipher = None


a = Analysis(['main_2.py'],
             pathex=['/Applications/XAMPP/xamppfiles/htdocs/python/website'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main_2',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='logo.ico')
app = BUNDLE(exe,
             name='main_2.app',
             icon='./logo.ico',
             bundle_identifier=None)
