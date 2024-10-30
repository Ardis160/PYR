state_data <- read.csv("state_x77.csv")
lm_model <- lm (Murder~ Life.Exp + Income + Population + Illiteracy + HS.Grad, data = state_data)
stat_1 <- summary(lm_model)
pred_1 <- predict(lm_model)

state_data_normalized <- data.Normalization(
  state_data %>% dplyr::select(-X, -Murder), type="n1", normalization="column"
  ) %>%
  mutate(state_data  %>%  dplyr::select(X, Murder))

lm_model_normalized <- lm (Murder~ Life.Exp + Income + Population + Illiteracy + HS.Grad, data = state_data_normalized)
stat_2 <- summary(lm_model_normalized)