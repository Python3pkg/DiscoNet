# -*- mode: python -*-
from kivy.deps import sdl2, glew
block_cipher = None


a = Analysis(['DiscoNet\\discoveryscan.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=['paramiko', 'openpyxl'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz, Tree('DiscoNet\\'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='discoveryscan',
          debug=False,
          strip=False,
          upx=False,
          console=True , icon='DiscoNet\\disco.ico')
