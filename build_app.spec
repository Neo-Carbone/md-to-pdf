# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['convert_md_to_pdf_app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['markdown', 'weasyprint', 'weasyprint.css', 'weasyprint.html', 'weasyprint.pdf', 'pymdownx', 'pymdownx.tasklist'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MarkdownToPDF',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(
    exe,
    name='MarkdownToPDF.app',
    icon=None,
    bundle_identifier='com.markdowntopdf.converter',
    version='1.0.0',
    info_plist={
        'CFBundleName': 'MarkdownToPDF',
        'CFBundleDisplayName': 'Markdown to PDF',
        'CFBundleGetInfoString': 'Convert Markdown files to styled PDF',
        'CFBundleIdentifier': 'com.markdowntopdf.converter',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': 'True',
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeName': 'Markdown Document',
                'CFBundleTypeRole': 'Editor',
                'LSItemContentTypes': ['net.daringfireball.markdown', 'public.plain-text'],
                'LSHandlerRank': 'Owner',
            }
        ],
    },
)

