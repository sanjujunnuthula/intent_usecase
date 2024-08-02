# from common import common_responsor
# from managers import file_manager, nlp_manager,text_pattern_manager
# from modules.image import image_parser, image_validator, image_responsor, image_constants
#
#
# def intent_on_image(arguments, files, form):
#     (error, image_file, image_url) = image_parser.parse_image_param_from_request(files, form)
#     if error:
#         return common_responsor.response_validation_error(error)
#
#     (error, image_source, is_file) = image_validator.validate_image_param_from_request(image_file, image_url)
#     if error:
#         return common_responsor.response_validation_error(error)
#
#     send_predictions = image_parser.parse_arguments_from_request(arguments)
#
#     (error, send_predictions) = image_validator.validate_arguments_from_request(send_predictions)
#     if error:
#         return common_responsor.response_validation_error(error)
#
#     if is_file:
#         input_image_path, input_image_name = file_manager.save_image_file_from_request(image_source)
#         #
#         # print("input_image_path", input_image_path)
#         # print("input_image_name", input_image_name)
#     else:
#         error, input_image_path, input_image_name = file_manager.download_and_save_image_url_from_request(image_source)
#         if error:
#             return common_responsor.response_validation_error(error)
#     # print("input_image_path45",input_image_path)
#     # print("input_image_name78",input_image_name)
#     (error, detection) = nlp_manager.detection_on_image(
#         input_image_path, input_image_name, send_predictions
#     )
#
#     # print("detection",detection)
#     file_manager.delete_local_file(input_image_path)
#     if error:
#         return common_responsor.response_validation_error(error)
#
#     if send_predictions == image_constants.SEND_PREDICTIONS_IMAGE:
#         # print("detection_raw_image",detection)
#         return image_responsor.send_file_from_directory(detection.output_url)
#     else:
#         return image_responsor.intent_on_image_success(detection, send_predictions)
