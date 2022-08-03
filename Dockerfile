FROM ubuntu:20.04

ENV LANG C.UTF-8
ENV PIPENV_VENV_IN_PROJECT 1
ENV TZ Asia/Tokyo

COPY . /app
WORKDIR /app

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
 && echo $TZ > /etc/timezone                       \
 && apt-get update -y                              \
 && apt-get install -y --no-install-recommends     \
    gettext                                        \
    libpq-dev                                      \
    postgresql                                     \
    postgresql-contrib                             \
    python3-pip                                    \
    python3.10-dev                                 \
    ufw                                            \
 && apt-get autoremove -y                          \
 && apt-get clean -y                               \
 && rm -rf /var/lib/apt/lists/*                    \
 && pip install pipenv                             \
 && pipenv install

CMD . /app/launch.sh
