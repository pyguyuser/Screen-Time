# Screen-Time


2 function option:

  def colormix():
      global R, G, B
      if R >= 225:
          if R <= 255 and G >= 30:
              R -= 5
              G += 5
          else:
              R += 5
              G += 5
      else:
          if R < 225 and G >= 30 or G >= 0 and B > 0:
              if G >= 225 or R == 30:
                  if G <= 255 and B >= 30 or G == 0 and B > 0:
                      if R == 30:
                          if G <= 30 and B <= 255:
                              if G == 0:
                                  B -= 5
                              else:
                                  G -= 5
                                  B -= 5
                          else:
                              G -= 5
                              B += 5
                      else:
                          G -= 5
                          R -= 5
                          B += 5
                  else:
                      R -= 5
                      G += 5
                      B += 5
              else:
                  R -= 5
                  G += 5
          else:
              R += 5
