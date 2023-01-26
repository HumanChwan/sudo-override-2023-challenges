FROM rastasheep/ubuntu-sshd

# Create new user
RUN adduser --disabled-password --gecos '' user
# Add some random password
RUN echo "user:know_your_man" | chpasswd
RUN passwd -n 9999 user

# Setup ssh and man
RUN apt-get update -y
RUN apt-get install man -y


# Downloading and installing cat manpage
RUN wget https://git.kernel.org/pub/scm/docs/man-pages/man-pages-posix.git/plain/man-pages-posix-2017/man1p/cat.1p \
    && cp cat.1p /usr/share/man/man1/cat.1p
RUN mandb

# put the flag in
RUN echo "sudo{c4n_y0u_d0_th4t_In_3m4cs_hUh}" > /flag.txt

# edit the bashrc
RUN echo "man cat; exit" > /home/user/.bashrc
RUN chown root:root /home/user/.bashrc
