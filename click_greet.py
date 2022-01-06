import click
import sys


def say_hello(name):
    # print와 같지만, python2역시 지원하기 위해 사용하는 click.echo
    click.echo("Hello, {}".format(name))


def say_goodbye(name):
    click.echo('Good bye, {}'.format(name))


# click 데코레이터
@click.option('--bye', is_flag=True, help="say good bye.")
@click.option('--hello', is_flag=True, help="say hello.")
@click.option('-v', '--version', is_flag=True, help="Show version of this program.")
@click.argument('name')
@click.command()
def main(name, version, hello, bye):

    if version:
        print('1.0.0')
        sys.exit()

    # 함수명과 인자명을 구분하기 위해 say_hello / say_goodbye로 함수명을 바꿈
    if bye:
        say_goodbye(name)
    else:
        say_hello(name)


if __name__ == "__main__":
    main()