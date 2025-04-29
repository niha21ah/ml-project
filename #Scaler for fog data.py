#Scaler for fog data

def scale_columns(df, cols):
    scaler = StandardScaler()
    scaled = df.copy()
    scaled[cols] = scaler.fit_transform(scaled[cols])
    return scaled
fog_scaled = scale_columns(fog, fog.drop(columns=['Date', 'Time', 'Label']).columns)
fog_scaled