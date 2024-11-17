from multiprocessing import Pool
import mrcfile
import numpy as np
import warnings
import os
import glob
import sys

warnings.simplefilter('ignore')
class InputNorm():
    def __init__(self, tomo_path, tomo_format, base_dir, norm_type):
        self.tomo_path = tomo_path
        self.tomo_format = tomo_format
        self.base_dir = base_dir
        self.norm_type = norm_type


        if self.norm_type == 'standardization':
            self.save_dir = os.path.join(self.base_dir, 'data_std')
        elif self.norm_type == 'normalization':
            self.save_dir = os.path.join(self.base_dir, 'data_norm')
        os.makedirs(self.save_dir, exist_ok=True)

        self.dir_list = [i.split('/')[-1] for i in glob.glob(self.tomo_path + '/*%s' % self.tomo_format)]
        print(self.dir_list)
        print('Total number of files: %d' % len(self.dir_list))

    # def single_handle(self, i):
    #     dir_name = self.dir_list[i]
    #     output_path = os.path.join(self.save_dir, dir_name)
        
    #     print(f'Starting normalization of {dir_name}')
        
    #     try:
    #         # Open input file with context manager
    #         with mrcfile.open(os.path.join(self.tomo_path, dir_name), permissive=True) as gm:
    #             if gm.data is None:
    #                 print(f'Error: No data in {dir_name}')
    #                 return False
                    
    #             # Load and normalize data
    #             data = np.array(gm.data, dtype=np.float32)
                
    #             if self.norm_type == 'standardization':
    #                 mean = data.mean()
    #                 std = data.std()
    #                 if std == 0:
    #                     print(f'Warning: Zero standard deviation in {dir_name}')
    #                     return False
    #                 data = (data - mean) / std
    #             elif self.norm_type == 'normalization':
    #                 min_val = data.min()
    #                 max_val = data.max()
    #                 if max_val == min_val:
    #                     print(f'Warning: Zero range in {dir_name}')
    #                     return False
    #                 data = (data - min_val) / (max_val - min_val)

    #             # Save normalized data
    #             with mrcfile.new(output_path, overwrite=True) as reconstruction_norm:
    #                 reconstruction_norm.set_data(data)
                    
    #             print(f'Successfully normalized {dir_name}')
    #             return True
                
    #     except Exception as e:
    #         print(f'Error processing {dir_name}: {str(e)}')
    #         return False
    #     finally:
    #         # Ensure memory is freed
    #         if 'data' in locals():
    #             del data

    # def handle_parallel(self):
    #     n_processes = min(len(self.dir_list), os.cpu_count() or 1)
    #     print(f'Starting normalization with {n_processes} processes')

    #     with Pool(n_processes) as p:
    #         try:
    #             results = p.map(self.single_handle, range(len(self.dir_list)))
    #             results.get(timeout=180)  # 1-hour timeout
    #         except TimeoutError:
    #             print('Normalization timed out. Skipping remaining tasks.')
    #             # Log the timeout error
    #             with open('normalization_errors.txt', 'a') as log_file:
    #                 log_file.write('Normalization timed out after 1 hour.\n')
    #             # Optionally terminate the pool if you don't want to continue
    #             # p.terminate()
    #         except Exception as e:
    #             print(f'An error occurred: {e}')
    #             # Log any other errors
    #             with open('normalization_errors.txt', 'a') as log_file:
    #                 log_file.write(f'An error occurred: {e}\n')
    #         finally:
    #             p.close()
    #             p.join()
    #             print("Finished normalizing all mrc files")
        
    #     # with Pool(n_processes) as p:
    #     #     try:
    #     #         results = p.map_async(self.single_handle, range(len(self.dir_list)))
    #     #         results.get(timeout=3600)  # 1 hour timeout
    #     #     except TimeoutError:
    #     #         print('Normalization timed out')
    #     #         p.terminate()
    #     #     finally:
    #     #         p.close()
    #     #         p.join()
                
    #     # Report results
    #     successes = sum(1 for r in results.get() if r)
    #     print(f'Normalized {successes}/{len(self.dir_list)} files successfully')

    def single_handle(self, i):
        dir_name = self.dir_list[i]
        with mrcfile.open(os.path.join(self.tomo_path, dir_name),
                          permissive=True) as gm:
            print('Processing %s' % dir_name)
            try:
                data = np.array(gm.data).astype(np.float32)
            except:
                data = np.array(gm.data).astype(np.float32)
            # print(data.shape)
            if self.norm_type == 'standardization':
                data -= data.mean()
                data /= data.std()
            elif self.norm_type == 'normalization':
                data -= data.min()
                data /= (data.max() - data.min())

            reconstruction_norm = mrcfile.new(
                os.path.join(self.save_dir, dir_name), overwrite=True)
            try:
                reconstruction_norm.set_data(data.astype(np.float32))
            except:
                reconstruction_norm.set_data(data.astype(np.float32))

            reconstruction_norm.close()
            print('%d/%d finished.' % (i + 1, len(self.dir_list)))
        print("Finished normalizing all mrc files")

    # def single_handle(self, i):
    #     dir_name = self.dir_list[i]
    #     print(f'Starting to process {dir_name}...')
    #     try:
    #         with mrcfile.open(os.path.join(self.tomo_path, dir_name), permissive=True) as gm:
    #             print(f'File {dir_name} opened successfully')
    #             try:
    #                 print(f'Loading data from {dir_name}, shape: {gm.data.shape}')
    #                 data = np.array(gm.data).astype(np.float32)
    #                 print(f'Data loaded successfully for {dir_name}')
    #             except Exception as e:
    #                 print(f'Error loading data for {dir_name}: {str(e)}')
    #                 data = np.array(gm.data).astype(np.float32)
                
    #             if self.norm_type == 'standardization':
    #                 print(f'Standardizing {dir_name}...')
    #                 data -= data.mean()
    #                 print(f'Mean subtracted for {dir_name}')
    #     except Exception as e:
    #         print(f'Failed to process {dir_name}: {str(e)}')


    # def handle_parallel(self):
    #     with Pool(len(self.dir_list)) as p:
    #         p.map(self.single_handle, np.arange(len(self.dir_list)).tolist())

    def handle_parallel(self):
       for item in np.arange(len(self.dir_list)).tolist():
           try:
               self.single_handle(item)
           except Exception as e:
                
                print(f'Error processing {item}: {str(e)}')


def norm_show(args):
    tomo_path, tomo_format, base_dir, norm_type, stdout = args
    if stdout is not None:
        save_stdout = sys.stdout
        save_stderr = sys.stderr
        sys.stdout = stdout
        sys.stderr = stdout

    pre_norm = InputNorm(tomo_path, tomo_format, base_dir, norm_type)
    pre_norm.handle_parallel()
    print('Standardization finished!')
    print('*' * 100)
    """
    try:
        pre_norm = InputNorm(tomo_path, tomo_format, base_dir, norm_type)
        pre_norm.handle_parallel()
        print('Standardization finished!')
        print('*' * 100)
    except:
        stdout.flush()
        stdout.write('Normalization Exception!')
        return 0
    """
    if stdout is not None:
        sys.stderr = save_stderr
        sys.stdout = save_stdout