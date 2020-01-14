from blinqr import fix_scaling, select_file, send

if __name__ == '__main__':
    fix_scaling()

    path = select_file()
    if not path:
        raise SystemExit

    with open(path, 'rb') as f:
        data = f.read()

    send(data)
