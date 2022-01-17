indow.fill(BLACK)
        window.blit(game_over_message, (WIDTH // 2 - game_over_message.get_width() // 2,
                                    HEIGHT // 2 - game_over_message.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(1000)
        menu = True
        print("lol")