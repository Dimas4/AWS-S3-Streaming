from subprocess import call

from smart_open import smart_open

from app.config.get_config import get_config
from app.generate.generate import generate


BASE_URL = "s3://{bucket}/{file}"


def main():
    config = get_config()
    bucket = config['bucket']
    host_bridge = config['host']['bridge']

    URL = BASE_URL.format(bucket=bucket['name'], file=bucket['file'])

    call(["aws", f"--endpoint-url=http://{host_bridge}:4572", "s3", "mb", f"s3://{bucket['name']}"])

    with smart_open(URL, 'wb', host=f'{host_bridge}:4572') as fout:
        for number in generate():
            print(number)
            print('=' * 200)
            fout.write(number.encode('utf-8'))

    print('Read')
    print('*' * 200)

    with smart_open(URL, 'r', host=f'{host_bridge}:4572') as fout:
        for line in fout:
            print(line)


if __name__ == '__main__':
    main()
