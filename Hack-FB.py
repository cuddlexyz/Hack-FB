import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))