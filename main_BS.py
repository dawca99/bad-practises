from PiContainer import PiContainer, calculate_pi, enumerate_pi

if __name__ == "__main__":

    my_pi = PiContainer()
    my_pi_2 = PiContainer()
    my_pi_3 = PiContainer()

    pi_gen = calculate_pi(5)
    for pi in pi_gen:
        my_pi.add_pi(pi)

    pi_gen_2 = calculate_pi(194)
    for pi in range(23):
        my_pi_2.add_pi(next(pi_gen_2))

    pi_gen_3 = calculate_pi(6)
    my_pi_3.add_pi(list(pi_gen_3))

    print('my first pi')
    enumerate_pi(my_pi)
    print('my second pi')
    enumerate_pi(my_pi_2)

    with open('Some-file.txt', 'w') as file:
        file.write(f'my best pi: {my_pi_3.a[-1]}')
        file.close()
