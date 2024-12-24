import os
import pkg_resources

# 获取数据文件路径的方法
def get_data_file_path(filename):
    return pkg_resources.resource_filename('autocnv', os.path.join('data', filename))

DEFAULT_SCORE = {
    'del': {
        '1A': 0, '1B': -0.6,
        '2A': 1, '2B': 0,
        '2C': -1, '2C-1': 0.9, '2C-2': 0,
        '2D': -1, '2D-1': 0, '2D-2': 0.9, '2D-3': 0.3, '2D-4': 0.9,
        '2E': 0, '2F': -1, '2G': 0, '2H': 0.15, '2I': 0, '2J': 0, '2K': 0.45,
        '3A': 0, '3B': 0.45, '3C': 0.9,
        '4O': -1,
        'PVS1': 0.9, 'PVS1_S': 0.45, 'PVS1_M': 0.3, 'PVS1_P': 0.15, 'PVS1_U': 0
    },
    'dup': {
        '1A': 0, '1B': -0.6,
        '2A': 1, '2B': 0,
        '2C': -1, '2C-1': 0.9, '2C-2': 0,
        '2D': -1, '2D-1': 0, '2D-2': 0.9, '2D-3': 0.3, '2D-4': 0.9,
        '2E': 0, '2F': -1, '2G': 0, '2H': 0, '2I': 0, '2J': 0, '2K': 0.45, '2L': 0,
        '3A': 0, '3B': 0.45, '3C': 0.9,
        '4O': -1,
        'PVS1': 0.9, 'PVS1_S': 0.45, 'PVS1_M': 0.3, 'PVS1_P': 0.15, 'PVS1_U': 0
    }
}


CYTO_BAND_FILE = get_data_file_path('cyto-band.bed.gz')

GENE_EXON_DATABASE = get_data_file_path('exon.sorted.bed.gz')

GENE_DATABASE = get_data_file_path('gene.sorted.bed.gz')

OMIM_GENE_DATABASE = get_data_file_path('omim-gene.sorted.bed.gz')

FUNC_REGION_DATABASE = get_data_file_path('func-region.sorted.gz')

HI_GENE_DATABASE = get_data_file_path('hi-gene.sorted.bed.gz')

HI_EXON_DATABASE = get_data_file_path('hi-exon.sorted.bed.gz')

HI_CDS_DATABASE = get_data_file_path('hi-cds.sorted.bed.gz')

CLINVAR_PATHOGENIC_DATABASE = get_data_file_path('clinvar-pathogenic.sorted.vcf.gz')

UHI_GENE_DATABASE = get_data_file_path('uhi-gene.sorted.bed.gz')

HI_REGION_DATABASE = get_data_file_path('hi-region.sorted.bed.gz')

UHI_REGION_DATABASE = get_data_file_path('uhi-region.sorted.bed.gz')

DECIPHER_GENE_DATABASE = get_data_file_path('decipher-gene.sorted.bed.gz')

TS_GENE_DATABASE = get_data_file_path('ts-gene.sorted.bed.gz')

TS_REGION_DATABASE = get_data_file_path('ts-region.sorted.bed.gz')

UTS_GENE_DATABASE = get_data_file_path('uts-gene.sorted.bed.gz')

UTS_REGION_DATABASE = get_data_file_path('uts-region.sorted.bed.gz')

DGV_GAIN_DATABASE = get_data_file_path('dgv-gain.sorted.bed.gz')

DGV_LOSS_DATABASE = get_data_file_path('dgv-loss.sorted.bed.gz')

GNOMAD_DEL_DATABASE = get_data_file_path('gnomad-del.sorted.bed.gz')

GNOMAD_DUP_DATABASE = get_data_file_path('gnomad-dup.sorted.bed.gz')

CNV_SYNDROME_DEL_DATABASE = get_data_file_path('cnv-syndrome-del.bed.gz')
CNV_SYNDROME_DUP_DATABASE = get_data_file_path('cnv-syndrome-dup.bed.gz')


try:
    from autocnv.local_settings import *
except ImportError:
    pass
