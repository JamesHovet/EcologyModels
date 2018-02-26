# -*- mode: python -*-

block_cipher = None


a = Analysis(['run.py'],
             pathex=['/Users/JamesHovet/Documents/Development/EcologyModels/MetaPopulation'],
             binaries=[],
             datas=[('metaPopulationModel', '.'), ('mesa', 'mesa')],
             hiddenimports=['mesa'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['IPython', 'matplotlib', 'scipy'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='run',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='run')
app = BUNDLE(coll,
             name='run.app',
             icon=None,
             bundle_identifier=None)
