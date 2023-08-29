operaciones = "8 + 6 = {}\n" \
              "8 - 6 = {}\n" \
              "8 * 6 = {}\n" \
              "8 / 6 = {:.2f}\n" \
              "8 % 6 = {}\n" \
              "8 // 6 = {}\n" \
              "8 ** 6 = {}"

resultado_formateado = operaciones.format(
    8 + 6,8 - 6,
    8 * 6,
    8 / 6,
    8 % 6,
    8 // 6,
    8 ** 6  )
print(resultado_formateado)
