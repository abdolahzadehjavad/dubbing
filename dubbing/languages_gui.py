# flake8: noqa

news = """
        """

language_data = {
    "english": {
        "description": """
        ### Dubbing
        """,
        "tutorial": """
        # **Instructions for use:**

        1. Upload a **video**, **subtitle file**, **audio file**, or provide a **URL link** to a video like YouTube.

        2. Choose the language in which you want to **translate the video**.

        3. Specify the **number of people speaking** in the video and **assign each one a text-to-speech voice** suitable for the translation language.

        4. Press the '**Translate**' button to obtain the results.

        ---

        # **support different TTS (Text-to-Speech) engines, which are:**
        - EDGE-TTS → format `en-AU-WilliamNeural-Male`
        - FACEBOOK MMS → format `en-facebook-mms VITS`
        - PIPER TTS → format `en_US-lessac-high VITS-onnx`
        - BARK → format `en_speaker_0-Male BARK`
        - OpenAI TTS → format `>alloy OpenAI-TTS`
        - Coqui XTTS → format `_XTTS_/AUTOMATIC.wav` → Only available for Chinese (Simplified), English, French, German, Italian, Portuguese, Polish, Turkish, Russian, Dutch, Czech, Arabic, Spanish, Hungarian, Korean and Japanese.

        ---

        # How to Use R.V.C. and R.V.C.2 Voices (Optional) 

        The goal is to apply a R.V.C. to the generated TTS (Text-to-Speech) 

        1. In the `Custom Voice R.V.C.` tab, download the models you need  You can use links from Hugging Face and Google Drive in formats like zip, pth, or index. You can also download complete HF space repositories, but this option is not very stable 

        2. Now, go to `Replace voice: TTS to R.V.C.` and check the `enable` box ✅ After this, you can choose the models you want to apply to each TTS speaker 

        3. Adjust the F0 method that will be applied to all R.V.C. 

        4. Press `APPLY CONFIGURATION` to apply the changes you made 

        5. Go back to the video translation tab and click on 'Translate' ▶️ Now, the translation will be done applying the R.V.C. 

        Tip: You can use `Test R.V.C.` to experiment and find the best TTS or configurations to apply to the R.V.C. 

        ---

        """,
        "tab_translate": "Video translation",
        "video_source": "Choose Video Source",
        "link_label": "Media link.",
        "link_info": "Example: www.youtube.com/watch?v=g_9rP985vbENUw",
        "link_ph": "URL goes here...",
        "dir_label": "Video Path.",
        "dir_info": "Example: /usr/home/my_video.mp4",
        "dir_ph": "Path goes here...",
        "sl_label": "Source language",
        "sl_info": "This is the original language of the video",
        "tat_label": "Translate audio to",
        "tat_info": "Select the target language and also make sure to choose the corresponding TTS for that language.",
        "num_speakers": "Select how many people are speaking in the video.",
        "min_sk": "Min speakers",
        "max_sk": "Max speakers",
        "tts_select": "Select the voice you want for each speaker.",
        "sk1": "TTS Speaker 1",
        "sk2": "TTS Speaker 2",
        "sk3": "TTS Speaker 3",
        "sk4": "TTS Speaker 4",
        "sk5": "TTS Speaker 5",
        "sk6": "TTS Speaker 6",
        "sk7": "TTS Speaker 7",
        "sk8": "TTS Speaker 8",
        "sk9": "TTS Speaker 9",
        "sk10": "TTS Speaker 10",
        "sk11": "TTS Speaker 11",
        "sk12": "TTS Speaker 12",
        "vc_title": "Voice Imitation in Different Languages",
        "vc_subtitle": """
        ### Replicate a person's voice across various languages.
        While effective with most voices when used appropriately, it may not achieve perfection in every case.
        Voice Imitation solely replicates the reference speaker's tone, excluding accent and emotion, which are governed by the base speaker TTS model and not replicated by the converter.
        This will take audio samples from the main audio for each speaker and process them.
        """,
        "vc_active_label": "Active Voice Imitation",
        "vc_active_info": "Active Voice Imitation: Replicates the original speaker's tone",
        "vc_method_label": "Method",
        "vc_method_info": "Select a method for Voice Imitation process",
        "vc_segments_label": "Max samples",
        "vc_segments_info": "Max samples: Is the number of audio samples that will be generated for the process, more is better but it can add noise",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: Applies vocal dereverb to the audio samples.",
        "vc_remove_label": "Remove previous samples",
        "vc_remove_info": "Remove previous samples: Remove the previous samples generated, so new ones need to be created.",
        "xtts_title": "Create a TTS based on an audio",
        "xtts_subtitle": "Upload an audio file of maximum 10 seconds with a voice. Using XTTS, a new TTS will be created with a voice similar to the provided audio file.",
        "xtts_file_label": "Upload a short audio with the voice",
        "xtts_name_label": "Name for the TTS",
        "xtts_name_info": "Use a simple name",
        "xtts_dereverb_label": "Dereverb audio",
        "xtts_dereverb_info": "Dereverb audio: Applies vocal dereverb to the audio",
        "xtts_button": "Process the audio and include it in the TTS selector",
        "xtts_footer": "Generate voice xtts automatically: You can use `_XTTS_/AUTOMATIC.wav` in the TTS selector to automatically generate segments for each speaker when generating the translation.",
        "extra_setting": "Advanced Settings",
        "acc_max_label": "Max Audio acceleration",
        "acc_max_info": "Maximum acceleration for translated audio segments to avoid overlapping. A value of 1.0 represents no acceleration",
        "acc_rate_label": "Acceleration Rate Regulation",
        "acc_rate_info": "Acceleration Rate Regulation: Adjusts acceleration to accommodate segments requiring less speed, maintaining continuity and considering next-start timing.",
        "or_label": "Overlap Reduction",
        "or_info": "Overlap Reduction: Ensures segments don't overlap by adjusting start times based on previous end times; could disrupt synchronization.",
        "aud_mix_label": "Audio Mixing Method",
        "aud_mix_info": "Mix original and translated audio files to create a customized, balanced output with two available mixing modes.",
        "vol_ori": "Volume original audio",
        "vol_tra": "Volume translated audio",
        "voiceless_tk_label": "Voiceless Track",
        "voiceless_tk_info": "Voiceless Track: Remove the original audio voices before combining it with the translated audio.",
        "sub_type": "Subtitle type",
        "soft_subs_label": "Soft Subtitles",
        "soft_subs_info": "Soft Subtitles: Optional subtitles that viewers can turn on or off while watching the video.",
        "burn_subs_label": "Burn Subtitles",
        "burn_subs_info": "Burn Subtitles: Embed subtitles into the video, making them a permanent part of the visual content.",
        "whisper_title": "Config transcription.",
        "lnum_label": "Literalize Numbers",
        "lnum_info": "Literalize Numbers: Replace numerical representations with their written equivalents in the transcript.",
        "scle_label": "Sound Cleanup",
        "scle_info": "Sound Cleanup: Enhance vocals, remove background noise before transcription for utmost timestamp precision. This operation may take time, especially with lengthy audio files.",
        "sd_limit_label": "Segment Duration Limit",
        "sd_limit_info": "Specify the maximum duration (in seconds) for each segment. The audio will be processed using VAD, limiting the duration for each segment chunk.",
        "asr_model_info": "It converts spoken language to text using the 'Whisper model' by default. Use a custom model, for example, by inputting the repository name 'BELLE-2/Belle-whisper-large-v3-zh' in the dropdown to utilize a Chinese language finetuned model. Find finetuned models on Hugging Face.",
        "ctype_label": "Compute type",
        "ctype_info": "Choosing smaller types like int8 or float16 can improve performance by reducing memory usage and increasing computational throughput, but may sacrifice precision compared to larger data types like float32.",
        "batchz_label": "Batch size",
        "batchz_info": "Reducing the batch size saves memory if your GPU has less VRAM and helps manage Out of Memory issues.",
        "tsscale_label": "Text Segmentation Scale",
        "tsscale_info": "Divide text into segments by sentences, words, or characters. Word and character segmentation offer finer granularity, useful for subtitles; disabling translation preserves original structure.",
        "srt_file_label": "Upload an SRT subtitle file (will be used instead of the transcription of Whisper)",
        "divide_text_label": "Redivide text segments by:",
        "divide_text_info": "(Experimental) Enter a separator to split existing text segments in the source language. The tool will identify occurrences and create new segments accordingly. Specify multiple separators using |, e.g.: !|?|...|。",
        "diarization_label": "Diarization model",
        "tr_process_label": "Translation process",
        "out_type_label": "Output type",
        "out_name_label": "File name",
        "out_name_info": "The name of the output file",
        "task_sound_label": "Task Status Sound",
        "task_sound_info": "Task Status Sound: Plays a sound alert indicating task completion or errors during execution.",
        "cache_label": "Retrieve Progress",
        "cache_info": "Retrieve Progress: Continue process from last checkpoint.",
        "preview_info": "Preview cuts the video to only 10 seconds for testing purposes. Please deactivate it to retrieve the full video duration.",
        "edit_sub_label": "Edit generated subtitles",
        "edit_sub_info": "Edit generated subtitles: Allows you to run the translation in 2 steps. First with the 'GET SUBTITLES AND EDIT' button, you get the subtitles to edit them, and then with the 'TRANSLATE' button, you can generate the video",
        "button_subs": "GET SUBTITLES AND EDIT",
        "editor_sub_label": "Generated subtitles",
        "editor_sub_info": "Feel free to edit the text in the generated subtitles here. You can make changes to the interface options before clicking the 'TRANSLATE' button, except for 'Source language', 'Translate audio to', and 'Max speakers', to avoid errors. Once you're finished, click the 'TRANSLATE' button.",
        "editor_sub_ph": "First press 'GET SUBTITLES AND EDIT' to get the subtitles",
        "button_translate": "TRANSLATE",
        "output_result_label": "DOWNLOAD TRANSLATED VIDEO",
        "sub_ori": "Subtitles",
        "sub_tra": "Translated subtitles",
        "ht_token_info": "One important step is to accept the license agreement for using Pyannote. You need to have an account on Hugging Face and accept the license to use the models: https://huggingface.co/pyannote/speaker-diarization and https://huggingface.co/pyannote/segmentation. Get your KEY TOKEN here: https://hf.co/settings/tokens",
        "ht_token_ph": "Token goes here...",
        "tab_docs": "Document translation",
        "docs_input_label": "Choose Document Source",
        "docs_input_info": "It can be PDF, DOCX, TXT, or text",
        "docs_source_info": "This is the original language of the text",
        "chunk_size_label": "Max number of characters that the TTS will process per segment",
        "chunk_size_info": "A value of 0 assigns a dynamic and more compatible value for the TTS.",
        "docs_button": "Start Language Conversion Bridge",
        "cv_url_info": "Automatically download the R.V.C. models from the URL. You can use links from HuggingFace or Drive, and you can include several links, each one separated by a comma. Example: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Replace voice: TTS to R.V.C.",
        "sec1_title": "### 1. To enable its use, mark it as enable.",
        "enable_replace": "Check this to enable the use of the models.",
        "sec2_title": "### 2. Select a voice that will be applied to each TTS of each corresponding speaker and apply the configurations.",
        "sec2_subtitle": "Depending on how many <TTS Speaker> you will use, each one needs its respective model. Additionally, there is an auxiliary one if for some reason the speaker is not detected correctly.",
        "cv_tts1": "Choose the voice to apply for Speaker 1.",
        "cv_tts2": "Choose the voice to apply for Speaker 2.",
        "cv_tts3": "Choose the voice to apply for Speaker 3.",
        "cv_tts4": "Choose the voice to apply for Speaker 4.",
        "cv_tts5": "Choose the voice to apply for Speaker 5.",
        "cv_tts6": "Choose the voice to apply for Speaker 6.",
        "cv_tts7": "Choose the voice to apply for Speaker 7.",
        "cv_tts8": "Choose the voice to apply for Speaker 8.",
        "cv_tts9": "Choose the voice to apply for Speaker 9.",
        "cv_tts10": "Choose the voice to apply for Speaker 10.",
        "cv_tts11": "Choose the voice to apply for Speaker 11.",
        "cv_tts12": "Choose the voice to apply for Speaker 12.",
        "cv_aux": "- Voice to apply in case a Speaker is not detected successfully.",
        "cv_button_apply": "APPLY CONFIGURATION",
        "tab_help": "Help",
    },
    "persian": {
        "description": """
        ### Dubbing
        """,
        "tutorial": """
        # **دستورالعمل استفاده:**

        1. یک **ویدئو**، **فایل زیرنویس**، **فایل صوتی** را آپلود کنید یا **لینک URL** به یک ویدئو مانند یوتیوب ارائه دهید.

        2. زبانی را که می‌خواهید **ویدئو را به آن ترجمه کنید** انتخاب کنید.

        3. تعداد **افراد گوینده** در ویدئو را مشخص کنید و **برای هرکدام یک صدای متن به گفتار مناسب** برای زبان ترجمه انتخاب کنید.

        4. دکمه '**ترجمه**' را فشار دهید تا نتایج را دریافت کنید.

        ---

        # ** موتور های تبدیل متن به گفتار که استفاده شده:**
        - EDGE-TTS → فرمت `en-AU-WilliamNeural-Male` 
        - FACEBOOK MMS → فرمت `en-facebook-mms VITS` 
        - PIPER TTS → فرمت `en_US-lessac-high VITS-onnx` 
        - BARK → فرمت `en_speaker_0-Male BARK` 
        - OpenAI TTS → فرمت `>alloy OpenAI-TTS` 
        - Coqui XTTS → فرمت `_XTTS_/AUTOMATIC.wav` → فقط برای چینی (ساده‌شده)، انگلیسی، فرانسوی، آلمانی، ایتالیایی، پرتغالی، لهستانی، ترکی، روسی، هلندی، چک، عربی، اسپانیایی، مجارستانی، کره‌ای و ژاپنی در دسترس است.

        ---

        # چگونه از صداهای R.V.C. و R.V.C.2 استفاده کنیم (اختیاری) 

        هدف اعمال R.V.C. به TTS تولید شده است

        1. در تب `Custom Voice R.V.C.` مدل‌های مورد نیاز را دانلود کنید می‌توانید از لینک‌های Hugging Face و Google Drive در قالب‌های zip، pth، یا index استفاده کنید. همچنین می‌توانید مخازن کامل HF را دانلود کنید، اما این گزینه خیلی پایدار نیست 😕

        2. حالا به `Replace voice: TTS to R.V.C.` بروید و جعبه `enable` را تیک بزنید پس از این، می‌توانید مدل‌هایی را که می‌خواهید به هر سخنگوی TTS اعمال کنید انتخاب کنید 

        3. روش F0 که برای همه R.V.C. اعمال خواهد شد تنظیم کنید

        4. دکمه `APPLY CONFIGURATION` را فشار دهید تا تغییرات اعمال شود

        5. به تب ترجمه ویدئو بازگردید و بر روی 'Translate' کلیک کنید ▶️ حالا ترجمه با اعمال R.V.C. انجام خواهد شد 

        نکته: می‌توانید از `Test R.V.C.` استفاده کنید تا بهترین TTS یا تنظیمات را برای اعمال به R.V.C. آزمایش و پیدا کنید

        ---

        """,
        "tab_translate": "ترجمه ویدئو",
        "video_source": "منبع ویدئو را انتخاب کنید",
        "link_label": "لینک رسانه.",
        "link_info": "مثال: www.youtube.com/watch?v=g_9rPvbEN955Uw",
        "link_ph": "لینک URL را اینجا وارد کنید...",
        "dir_label": "مسیر ویدئو.",
        "dir_info": "مثال: /usr/home/my_video.mp4",
        "dir_ph": "مسیر را اینجا وارد کنید...",
        "sl_label": "زبان مبدا",
        "sl_info": "این زبان اصلی ویدئو است",
        "tat_label": "ترجمه صوتی به",
        "tat_info": "زبان مقصد را انتخاب کنید و همچنین مطمئن شوید که TTS مربوط به آن زبان را انتخاب کنید.",
        "num_speakers": "تعداد افراد گوینده در ویدئو را انتخاب کنید.",
        "min_sk": "حداقل گوینده‌ها",
        "max_sk": "حداکثر گوینده‌ها",
        "tts_select": "صدای مورد نظر برای هر گوینده را انتخاب کنید.",
        "sk1": "گوینده TTS 1",
        "sk2": "گوینده TTS 2",
        "sk3": "گوینده TTS 3",
        "sk4": "گوینده TTS 4",
        "sk5": "گوینده TTS 5",
        "sk6": "گوینده TTS 6",
        "sk7": "گوینده TTS 7",
        "sk8": "گوینده TTS 8",
        "sk9": "گوینده TTS 9",
        "sk10": "گوینده TTS 10",
        "sk11": "گوینده TTS 11",
        "sk12": "گوینده TTS 12",
        "vc_title": "تقلید صدا در زبان‌های مختلف",
        "vc_subtitle": """
        ### صدای یک فرد را در زبان‌های مختلف بازتولید کنید.
        در حالی که با اکثر صداها به درستی کار می‌کند، ممکن است در هر مورد به صورت کامل عمل نکند.
        تقلید صدا تنها لحن گوینده مرجع را بازتولید می‌کند، بدون لهجه و احساسات که توسط مدل پایه TTS تعیین می‌شوند و توسط مبدل بازتولید نمی‌شوند.
        این کار نمونه‌های صوتی را از صدای اصلی هر گوینده گرفته و پردازش می‌کند.
        """,
        "vc_active_label": "تقلید صدا فعال است",
        "vc_active_info": "تقلید صدا فعال: لحن گوینده اصلی را بازتولید می‌کند",
        "vc_method_label": "روش",
        "vc_method_info": "یک روش برای فرآیند تقلید صدا انتخاب کنید",
        "vc_segments_label": "حداکثر نمونه‌ها",
        "vc_segments_info": "حداکثر نمونه‌ها: تعداد نمونه‌های صوتی که برای فرآیند تولید خواهند شد، بیشتر بهتر است اما ممکن است نویز اضافه کند",
        "vc_dereverb_label": "حذف اکو",
        "vc_dereverb_info": "حذف اکو: حذف اکو صوتی از نمونه‌های صوتی.",
        "vc_remove_label": "حذف نمونه‌های قبلی",
        "vc_remove_info": "حذف نمونه‌های قبلی: حذف نمونه‌های قبلی تولید شده، بنابراین نمونه‌های جدید نیاز به تولید دارند.",
        "xtts_title": "ایجاد TTS بر اساس یک فایل صوتی",
        "xtts_subtitle": "یک فایل صوتی کوتاه با صدای حداکثر 10 ثانیه آپلود کنید. با استفاده از XTTS، یک TTS جدید با صدای مشابه به فایل صوتی ارائه شده ایجاد خواهد شد.",
        "xtts_file_label": "یک فایل صوتی کوتاه با صدا آپلود کنید",
        "xtts_name_label": "نام برای TTS",
        "xtts_name_info": "یک نام ساده استفاده کنید",
        "xtts_dereverb_label": "حذف اکو صوتی",
        "xtts_dereverb_info": "حذف اکو صوتی: حذف اکو از صوت",
        "xtts_button": "پردازش صوت و افزودن آن به انتخابگر TTS",
        "xtts_footer": "تولید صدای XTTS به طور خودکار: می‌توانید از `_XTTS_/AUTOMATIC.wav` در انتخابگر TTS برای تولید خودکار بخش‌ها برای هر گوینده هنگام تولید ترجمه استفاده کنید.",
        "extra_setting": "تنظیمات پیشرفته",
        "acc_max_label": "حداکثر شتاب صوتی",
        "acc_max_info": "حداکثر شتاب برای بخش‌های صوتی ترجمه شده برای جلوگیری از تداخل. مقدار 1.0 نمایانگر بدون شتاب است",
        "acc_rate_label": "تنظیم نرخ شتاب",
        "acc_rate_info": "تنظیم نرخ شتاب: تنظیم شتاب برای سازگاری با بخش‌هایی که نیاز به سرعت کمتری دارند، حفظ پیوستگی و در نظر گرفتن زمان شروع بعدی.",
        "or_label": "کاهش تداخل",
        "or_info": "کاهش تداخل: اطمینان از عدم تداخل بخش‌ها با تنظیم زمان شروع بر اساس زمان پایان قبلی؛ ممکن است همگام‌سازی را مختل کند.",
        "aud_mix_label": "روش ترکیب صوتی",
        "aud_mix_info": "میکس فایل‌های صوتی اصلی و ترجمه شده برای ایجاد خروجی سفارشی و متعادل با دو حالت میکس موجود.",
        "vol_ori": "حجم صدای اصلی",
        "vol_tra": "حجم صدای ترجمه شده",
        "voiceless_tk_label": "مسیر بدون صدا",
        "voiceless_tk_info": "مسیر بدون صدا: حذف صدای اصلی قبل از ترکیب آن با صدای ترجمه شده.",
        "sub_type": "نوع زیرنویس",
        "soft_subs_label": "زیرنویس نرم",
        "soft_subs_info": "زیرنویس نرم: زیرنویس‌های اختیاری که بینندگان می‌توانند آنها را هنگام تماشا روشن یا خاموش کنند.",
        "burn_subs_label": "زیرنویس سوخته",
        "burn_subs_info": "زیرنویس سوخته: تعبیه زیرنویس‌ها در ویدئو، که آنها را به بخشی دائمی از محتوای بصری تبدیل می‌کند.",
        "whisper_title": "پیکربندی رونوشت.",
        "lnum_label": "نوشتاری اعداد",
        "lnum_info": "نوشتاری اعداد: جایگزین نمایش عددی با معادل‌های نوشتاری آنها در رونوشت.",
        "scle_label": "پاکسازی صدا",
        "scle_info": "پاکسازی صدا: تقویت صداها، حذف نویز پس‌زمینه قبل از رونوشت برای دقت زمان‌بندی بالا. این عملیات ممکن است زمان ببرد، به ویژه با فایل‌های صوتی طولانی.",
        "sd_limit_label": "حداکثر مدت زمان بخش",
        "sd_limit_info": "حداکثر مدت زمان برای هر بخش را مشخص کنید. صوت با استفاده از VAD پردازش خواهد شد، و مدت زمان برای هر بخش محدود خواهد شد.",
        "asr_model_info": "این مدل زبان گفتاری را به متن تبدیل می‌کند و از مدل 'Whisper' به‌صورت پیش‌فرض استفاده می‌کند. از یک مدل سفارشی استفاده کنید، برای مثال، با وارد کردن نام مخزن 'BELLE-2/Belle-whisper-large-v3-zh' در لیست کشویی برای استفاده از مدل چینی فاین‌تیون شده. مدل‌های فاین‌تیون شده را در Hugging Face پیدا کنید.",
        "ctype_label": "نوع محاسبه",
        "ctype_info": "انتخاب انواع کوچکتر مانند int8 یا float16 می‌تواند عملکرد را با کاهش استفاده از حافظه و افزایش توان محاسباتی بهبود بخشد، اما ممکن است دقت را نسبت به انواع داده‌های بزرگ‌تر مانند float32 فدا کند.",
        "batchz_label": "اندازه دسته",
        "batchz_info": "کاهش اندازه دسته حافظه را ذخیره می‌کند اگر GPU شما VRAM کمتری دارد و کمک می‌کند به مدیریت مشکلات کمبود حافظه.",
        "tsscale_label": "مقیاس بخش‌بندی متن",
        "tsscale_info": "تقسیم متن به بخش‌ها با جملات، کلمات، یا کاراکترها. بخش‌بندی کلمه و کاراکتر دانه‌بندی بیشتری ارائه می‌دهد که برای زیرنویس‌ها مفید است؛ غیرفعال کردن ترجمه ساختار اصلی را حفظ می‌کند.",
        "srt_file_label": "یک فایل زیرنویس SRT آپلود کنید (به جای رونوشت Whisper استفاده خواهد شد)",
        "divide_text_label": "تقسیم مجدد بخش‌های متن توسط:",
        "divide_text_info": "(آزمایشی) یک جداکننده برای تقسیم بخش‌های موجود متن در زبان منبع وارد کنید. ابزار وقوع‌ها را شناسایی کرده و بخش‌های جدید را بر اساس آن ایجاد می‌کند. چندین جداکننده را با | مشخص کنید، به عنوان مثال: !|?|...|。",
        "diarization_label": "مدل دیاریزیشن",
        "tr_process_label": "فرآیند ترجمه",
        "out_type_label": "نوع خروجی",
        "out_name_label": "نام فایل",
        "out_name_info": "نام فایل خروجی",
        "task_sound_label": "صدای وضعیت کار",
        "task_sound_info": "صدای وضعیت کار: پخش صدای هشدار نشان‌دهنده تکمیل کار یا خطاها در حین اجرا.",
        "cache_label": "بازیابی پیشرفت",
        "cache_info": "بازیابی پیشرفت: ادامه فرآیند از آخرین نقطه توقف.",
        "preview_info": "پیش‌نمایش ویدئو را به 10 ثانیه برای آزمایش برش می‌دهد. لطفاً آن را غیرفعال کنید تا ویدئوی کامل را دریافت کنید.",
        "edit_sub_label": "ویرایش زیرنویس‌های تولید شده",
        "edit_sub_info": "ویرایش زیرنویس‌های تولید شده: به شما امکان می‌دهد ترجمه را در دو مرحله انجام دهید. ابتدا با دکمه 'GET SUBTITLES AND EDIT' زیرنویس‌ها را بگیرید و ویرایش کنید، و سپس با دکمه 'TRANSLATE' ویدئو را تولید کنید",
        "button_subs": "GET SUBTITLES AND EDIT",
        "editor_sub_label": "زیرنویس‌های تولید شده",
        "editor_sub_info": "می‌توانید متن زیرنویس‌های تولید شده را اینجا ویرایش کنید. قبل از کلیک بر روی دکمه 'TRANSLATE' می‌توانید تغییرات را در گزینه‌های رابط ایجاد کنید، به جز 'زبان منبع'، 'ترجمه صوتی به' و 'حداکثر گوینده‌ها'، تا از بروز خطاها جلوگیری شود. پس از اتمام، دکمه 'TRANSLATE' را فشار دهید.",
        "editor_sub_ph": "ابتدا دکمه 'GET SUBTITLES AND EDIT' را فشار دهید تا زیرنویس‌ها را دریافت کنید",
        "button_translate": "TRANSLATE",
        "output_result_label": "دانلود ویدئوی ترجمه شده",
        "sub_ori": "زیرنویس‌ها",
        "sub_tra": "زیرنویس‌های ترجمه شده",
        "ht_token_info": "یکی از مراحل مهم قبول موافقتنامه مجوز برای استفاده از Pyannote است. شما نیاز به داشتن یک حساب کاربری در Hugging Face و قبول مجوز برای استفاده از مدل‌ها دارید: https://huggingface.co/pyannote/speaker-diarization و https://huggingface.co/pyannote/segmentation. کلید TOKEN خود را اینجا بگیرید: https://hf.co/settings/tokens",
        "ht_token_ph": "کلید TOKEN را اینجا وارد کنید...",
        "tab_docs": "ترجمه اسناد",
        "docs_input_label": "منبع سند را انتخاب کنید",
        "docs_input_info": "می‌تواند PDF، DOCX، TXT، یا متن باشد",
        "docs_source_info": "این زبان اصلی متن است",
        "chunk_size_label": "حداکثر تعداد کاراکترهایی که TTS در هر بخش پردازش خواهد کرد",
        "chunk_size_info": "مقدار 0 یک مقدار پویا و سازگارتر برای TTS اختصاص می‌دهد.",
        "docs_button": "شروع پل تبدیل زبان",
        "cv_url_info": "مدل‌های R.V.C. را به صورت خودکار از URL دانلود کنید. می‌توانید از لینک‌های HuggingFace یا Drive استفاده کنید و می‌توانید چندین لینک را شامل کنید، هرکدام با کاما جدا شده باشند. مثال: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "تعویض صدا: TTS به R.V.C.",
        "sec1_title": "### 1. برای فعال‌سازی استفاده، آن را به عنوان فعال علامت بزنید.",
        "enable_replace": "این را بررسی کنید تا استفاده از مدل‌ها فعال شود.",
        "sec2_title": "### 2. صدایی را که به هر TTS هر گوینده اعمال خواهد شد انتخاب کنید و تنظیمات را اعمال کنید.",
        "sec2_subtitle": "بسته به تعداد <گوینده TTS> که استفاده می‌کنید، هرکدام به مدل مربوطه خود نیاز دارند. علاوه بر این، یک مدل کمکی نیز وجود دارد که در صورت عدم تشخیص صحیح گوینده استفاده می‌شود.",
        "cv_tts1": "صدایی را برای گوینده 1 انتخاب کنید.",
        "cv_tts2": "صدایی را برای گوینده 2 انتخاب کنید.",
        "cv_tts3": "صدایی را برای گوینده 3 انتخاب کنید.",
        "cv_tts4": "صدایی را برای گوینده 4 انتخاب کنید.",
        "cv_tts5": "صدایی را برای گوینده 5 انتخاب کنید.",
        "cv_tts6": "صدایی را برای گوینده 6 انتخاب کنید.",
        "cv_tts7": "صدایی را برای گوینده 7 انتخاب کنید.",
        "cv_tts8": "صدایی را برای گوینده 8 انتخاب کنید.",
        "cv_tts9": "صدایی را برای گوینده 9 انتخاب کنید.",
        "cv_tts10": "صدایی را برای گوینده 10 انتخاب کنید.",
        "cv_tts11": "صدایی را برای گوینده 11 انتخاب کنید.",
        "cv_tts12": "صدایی را برای گوینده 12 انتخاب کنید.",
        "cv_aux": "- صدایی که در صورت عدم تشخیص موفقیت‌آمیز گوینده اعمال خواهد شد.",
        "cv_button_apply": "اعمال تنظیمات",
        "tab_help": "راهنمایی",
    },
}
